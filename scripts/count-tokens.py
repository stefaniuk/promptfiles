#!/usr/bin/env python3
"""
Count LLM tokens in markdown files loaded by Copilot.

This script traverses specified directories for *.md files and estimates
the token count using tiktoken (OpenAI's tokeniser). It provides a summary
suitable for understanding context window usage.

Usage:
    python scripts/count-tokens.py [--model MODEL] [--sort-by {tokens,path}] [PATHS...]

Examples:
    python scripts/count-tokens.py
    python scripts/count-tokens.py .github .specify
    python scripts/count-tokens.py --model gpt-4o --sort-by tokens
"""

from __future__ import annotations

import argparse
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

# Model encoding mappings for common models
MODEL_ENCODINGS = {
    "gpt-4o": "o200k_base",
    "gpt-4o-mini": "o200k_base",
    "gpt-4-turbo": "cl100k_base",
    "gpt-4": "cl100k_base",
    "gpt-3.5-turbo": "cl100k_base",
    "claude-3": "cl100k_base",  # Approximate; Claude uses similar tokenisation
    "claude-3.5": "cl100k_base",
}


@dataclass
class FileTokenCount:
    """Token count result for a single file."""

    path: Path
    tokens: int
    chars: int


def get_encoding(model: str) -> tiktoken.Encoding:
    """Get the tiktoken encoding for a given model."""
    encoding_name = MODEL_ENCODINGS.get(model, "cl100k_base")
    return tiktoken.get_encoding(encoding_name)


def count_tokens_in_file(file_path: Path, encoding: tiktoken.Encoding) -> FileTokenCount:
    """Count tokens in a single file."""
    try:
        content = file_path.read_text(encoding="utf-8")
        tokens = len(encoding.encode(content))
        return FileTokenCount(path=file_path, tokens=tokens, chars=len(content))
    except (OSError, UnicodeDecodeError) as err:
        sys.stderr.write(f"Warning: Could not read {file_path}: {err}\n")
        return FileTokenCount(path=file_path, tokens=0, chars=0)


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
    model: str,
    sort_by: str,
) -> None:
    """Print the token count results in a readable format."""
    if sort_by == "tokens":
        results = sorted(results, key=lambda r: r.tokens, reverse=True)
    else:
        results = sorted(results, key=lambda r: str(r.path))

    total_tokens = sum(r.tokens for r in results)
    total_chars = sum(r.chars for r in results)
    total_files = len(results)

    # Calculate column widths
    max_path_len = max(len(str(r.path.relative_to(base_dir))) for r in results) if results else 0
    max_tokens_len = max(len(format_number(r.tokens)) for r in results) if results else 0

    # Print header
    print(f"\n{'=' * 70}")
    print(f"Token Count Report (Model: {model})")
    print(f"{'=' * 70}\n")

    # Print per-file breakdown
    print(f"{'File':<{max_path_len}}  {'Tokens':>{max_tokens_len}}  {'Chars':>10}")
    print(f"{'-' * max_path_len}  {'-' * max_tokens_len}  {'-' * 10}")

    for result in results:
        rel_path = str(result.path.relative_to(base_dir))
        print(
            f"{rel_path:<{max_path_len}}  "
            f"{format_number(result.tokens):>{max_tokens_len}}  "
            f"{format_number(result.chars):>10}"
        )

    # Print summary
    print(f"\n{'-' * 70}")
    print(f"{'TOTAL':<{max_path_len}}  {format_number(total_tokens):>{max_tokens_len}}  {format_number(total_chars):>10}")
    print(f"\nSummary:")
    print(f"  Files scanned:  {total_files}")
    print(f"  Total tokens:   {format_number(total_tokens)}")
    print(f"  Total chars:    {format_number(total_chars)}")
    print(f"  Avg tokens/file: {total_tokens // total_files if total_files else 0}")

    # Context window guidance
    print(f"\nContext Window Reference:")
    print(f"  GPT-4o:         128K tokens ({total_tokens / 128_000 * 100:.1f}% usage)")
    print(f"  GPT-4 Turbo:    128K tokens ({total_tokens / 128_000 * 100:.1f}% usage)")
    print(f"  Claude 3.5:     200K tokens ({total_tokens / 200_000 * 100:.1f}% usage)")
    print(f"  Claude 3 Opus:  200K tokens ({total_tokens / 200_000 * 100:.1f}% usage)")


def print_by_directory(
    results: list[FileTokenCount],
    base_dir: Path,
) -> None:
    """Print token counts grouped by top-level directory."""
    dir_totals: dict[str, int] = {}

    for result in results:
        rel_path = result.path.relative_to(base_dir)
        top_dir = rel_path.parts[0] if len(rel_path.parts) > 1 else "(root)"
        dir_totals[top_dir] = dir_totals.get(top_dir, 0) + result.tokens

    print("\nTokens by Directory:")
    print(f"  {'Directory':<30}  {'Tokens':>12}")
    print(f"  {'-' * 30}  {'-' * 12}")

    for directory, tokens in sorted(dir_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {directory:<30}  {format_number(tokens):>12}")


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
        "--model",
        default="gpt-4o",
        choices=list(MODEL_ENCODINGS.keys()),
        help="Model to use for tokenisation (default: gpt-4o)",
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

    # Get encoding for the specified model
    encoding = get_encoding(args.model)

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
    print_results(results, base_dir, args.model, args.sort_by)
    print_by_directory(results, base_dir)

    return 0


if __name__ == "__main__":
    sys.exit(main())
