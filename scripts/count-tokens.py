#!/usr/bin/env python3
"""
Count LLM tokens in markdown files loaded by Copilot.

This script traverses specified directories for *.md files and estimates
the token count using tiktoken (OpenAI's tokeniser). It provides a summary
suitable for understanding context window usage.

Usage:
    python scripts/count-tokens.py [--sort-by {tokens,path}] [PATHS...]

Examples:
    python scripts/count-tokens.py
    python scripts/count-tokens.py .github .specify
    python scripts/count-tokens.py --sort-by tokens
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import tiktoken
except ImportError:
    sys.stderr.write(
        "Error: tiktoken is required. Install with: pip install tiktoken\n"
    )
    sys.exit(1)


# Default directories where Copilot loads prompt files from
DEFAULT_SEARCH_PATHS = [
    ".github",
    ".specify",
    "docs",
]

# Use a single encoding for reporting to keep outputs consistent
ENCODING_NAME = "o200k_base"
CONTEXT_WINDOW_TOKENS = 200_000

# Pattern to match instruction identifiers like [ID-<prefix>-NNN]
IDENTIFIER_PATTERN = re.compile(r"\[[A-Z]{2,3}-[A-Z]{1,4}-\d{3}[a-z]?\]")


@dataclass
class FileTokenCount:
    """Token count result for a single file."""

    path: Path
    tokens: int
    tokens_no_ids: int  # Token count with identifiers stripped
    chars: int


def strip_identifiers(content: str) -> str:
    """Remove instruction identifiers like [ID-<prefix>-NNN] from content."""
    return IDENTIFIER_PATTERN.sub("", content)


def get_encoding() -> tiktoken.Encoding:
    """Get the token encoding used for all counts."""
    return tiktoken.get_encoding(ENCODING_NAME)


def count_tokens_in_file(file_path: Path, encoding: tiktoken.Encoding) -> FileTokenCount:
    """Count tokens in a single file, both with and without identifiers."""
    try:
        content = file_path.read_text(encoding="utf-8")
        tokens = len(encoding.encode(content))
        content_stripped = strip_identifiers(content)
        tokens_no_ids = len(encoding.encode(content_stripped))
        return FileTokenCount(
            path=file_path,
            tokens=tokens,
            tokens_no_ids=tokens_no_ids,
            chars=len(content),
        )
    except (OSError, UnicodeDecodeError) as err:
        sys.stderr.write(f"Warning: Could not read {file_path}: {err}\n")
        return FileTokenCount(path=file_path, tokens=0, tokens_no_ids=0, chars=0)


def find_markdown_files(base_path: Path) -> list[Path]:
    """Find all markdown files recursively under the given path."""
    if not base_path.exists():
        return []
    if base_path.is_file() and base_path.suffix == ".md":
        return [base_path]
    return sorted(base_path.rglob("*.md"))


def format_number(num: int) -> str:
    """Format a number with thousands separators."""
    return f"{num:,}"


def print_results(
    results: list[FileTokenCount],
    base_dir: Path,
    sort_by: str,
) -> None:
    """Print the token count results in a readable format."""
    if sort_by == "tokens":
        results = sorted(results, key=lambda r: r.tokens, reverse=True)
    else:
        results = sorted(results, key=lambda r: str(r.path))

    total_tokens = sum(r.tokens for r in results)
    total_tokens_no_ids = sum(r.tokens_no_ids for r in results)
    total_chars = sum(r.chars for r in results)
    total_files = len(results)

    # Calculate column widths (include totals to ensure alignment)
    max_path_len = max(len(str(r.path.relative_to(base_dir))) for r in results) if results else 0
    max_tokens_len = max(
        max((len(format_number(r.tokens)) for r in results), default=0),
        len(format_number(total_tokens)),
    )
    max_no_ids_len = max(
        max((len(format_number(r.tokens_no_ids)) for r in results), default=0),
        len(format_number(total_tokens_no_ids)),
    )
    max_chars_len = max(
        max((len(format_number(r.chars)) for r in results), default=0),
        len(format_number(total_chars)),
    )

    # Print header
    print("\nToken Count Report (200K context window)\n")

    # Print per-file breakdown
    print(
        f"{'File':<{max_path_len}}  "
        f"{'Tokens':>{max_tokens_len}}  "
        f"{'No IDs':>{max_no_ids_len}}  "
        f"{'Chars':>{max_chars_len}}"
    )
    print(
        f"{'-' * max_path_len}  "
        f"{'-' * max_tokens_len}  "
        f"{'-' * max_no_ids_len}  "
        f"{'-' * max_chars_len}"
    )

    for result in results:
        rel_path = str(result.path.relative_to(base_dir))
        print(
            f"{rel_path:<{max_path_len}}  "
            f"{format_number(result.tokens):>{max_tokens_len}}  "
            f"{format_number(result.tokens_no_ids):>{max_no_ids_len}}  "
            f"{format_number(result.chars):>{max_chars_len}}"
        )

    # Print summary
    print(
        f"\n{'-' * max_path_len}  "
        f"{'-' * max_tokens_len}  "
        f"{'-' * max_no_ids_len}  "
        f"{'-' * max_chars_len}"
    )
    print(
        f"{'TOTAL':<{max_path_len}}  "
        f"{format_number(total_tokens):>{max_tokens_len}}  "
        f"{format_number(total_tokens_no_ids):>{max_no_ids_len}}  "
        f"{format_number(total_chars):>{max_chars_len}}"
    )
    print(f"\nSummary:")
    print(f"  Files scanned:   {total_files}")
    print(f"  Total tokens:    {format_number(total_tokens)}")
    print(f"  Without IDs:     {format_number(total_tokens_no_ids)}")
    print(f"  Total chars:     {format_number(total_chars)}")
    print(f"  Avg tokens/file: {total_tokens // total_files if total_files else 0}")

    # Context window guidance
    usage_pct = total_tokens / CONTEXT_WINDOW_TOKENS * 100
    usage_no_ids_pct = total_tokens_no_ids / CONTEXT_WINDOW_TOKENS * 100
    print(f"\nContext window usage: {usage_pct:.1f}% (without IDs: {usage_no_ids_pct:.1f}%)")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Count LLM tokens in markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_SEARCH_PATHS,
        help=f"Paths to search (default: {', '.join(DEFAULT_SEARCH_PATHS)})",
    )
    parser.add_argument(
        "--sort-by",
        choices=["tokens", "path"],
        default="path",
        help="Sort results by tokens or path (default: path)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Search all *.md files in the repository",
    )
    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()

    # Determine base directory (repository root)
    base_dir = Path.cwd()

    # Get encoding for the canonical model
    encoding = get_encoding()

    # Collect all markdown files
    all_files: list[Path] = []

    if args.all:
        all_files = find_markdown_files(base_dir)
    else:
        for path_str in args.paths:
            search_path = base_dir / path_str
            all_files.extend(find_markdown_files(search_path))

    if not all_files:
        sys.stderr.write("No markdown files found.\n")
        return 1

    # Remove duplicates and sort
    all_files = sorted(set(all_files))

    # Count tokens in each file
    results = [count_tokens_in_file(f, encoding) for f in all_files]

    # Print results
    print_results(results, base_dir, args.sort_by)
    print("")

    return 0


if __name__ == "__main__":
    sys.exit(main())
