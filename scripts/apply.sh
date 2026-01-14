#!/bin/bash

set -euo pipefail

# Copy prompt files assets to a destination repository.
#
# Usage:
#   $ [options] ./scripts/apply.sh <destination-directory>
#
# Arguments:
#   destination-directory   Target directory (absolute or relative path)
#
# Options:
#   VERBOSE=true            # Show all the executed commands, default is 'false'
#
# Copies:
#   - Agent files (.github/agents)
#   - Instruction files (.github/instructions and include)
#   - Prompt files (.github/prompts)
#   - Skills files (.github/skills, recursively)
#   - copilot-instructions.md
#   - constitution.md
#   - adr-template.md
#   - docs/.gitignore
#
# Exit codes:
#   0 - All files copied successfully
#   1 - Missing or invalid arguments
#
# Examples:
#   $ ./scripts/apply.sh /path/to/my-project
#   $ ./scripts/apply.sh ../my-project
#   $ VERBOSE=true ./scripts/apply.sh ~/projects/my-app

# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

AGENTS_DIR="${REPO_ROOT}/.github/agents"
INSTRUCTIONS_DIR="${REPO_ROOT}/.github/instructions"
PROMPTS_DIR="${REPO_ROOT}/.github/prompts"
SKILLS_DIR="${REPO_ROOT}/.github/skills"
COPILOT_INSTRUCTIONS="${REPO_ROOT}/.github/copilot-instructions.md"
CONSTITUTION="${REPO_ROOT}/.specify/memory/constitution.md"
ADR_TEMPLATE="${REPO_ROOT}/docs/adr/adr-template.md"
DOCS_GITIGNORE="${REPO_ROOT}/docs/.gitignore"

# ==============================================================================

# Main entry point for the script.
function main() {

  if [[ $# -ne 1 ]]; then
    print-usage
    exit 1
  fi

  local destination="$1"

  # Handle relative paths by converting to absolute
  if [[ "${destination}" != /* ]]; then
    destination="$(cd "$(pwd)" && cd "$(dirname "${destination}")" 2>/dev/null && pwd)/$(basename "${destination}")" || destination="$(pwd)/${destination}"
  fi

  # Expand ~ to home directory
  destination="${destination/#\~/$HOME}"

  # Validate destination
  if [[ -z "${destination}" ]]; then
    print-error "Destination directory cannot be empty"
  fi

  # Create destination if it doesn't exist
  if [[ ! -d "${destination}" ]]; then
    print-info "Creating destination directory: ${destination}"
    mkdir -p "${destination}"
  fi

  echo "Applying prompt files to: ${destination}"
  echo

  copy-agents "${destination}"
  copy-instructions "${destination}"
  copy-prompts "${destination}"
  copy-skills "${destination}"
  copy-copilot-instructions "${destination}"
  copy-constitution "${destination}"
  copy-adr-template "${destination}"
  copy-docs-gitignore "${destination}"

  echo
  echo "Done. Assets copied to ${destination}"
}

# ==============================================================================

# Print usage information.
function print-usage() {

  cat <<EOF
Usage: $(basename "$0") <destination-directory>

Copy prompt files assets to a destination repository.

Arguments:
    destination-directory   Target directory (absolute or relative path)

Examples:
    $(basename "$0") /path/to/my-project
    $(basename "$0") ../my-project
    VERBOSE=true $(basename "$0") ~/projects/my-app
EOF
}

# Print an error message to stderr and exit.
# Arguments:
#   $1=[error message to display]
function print-error() {

  echo "Error: $1" >&2
  exit 1
}

# Print an informational message.
# Arguments:
#   $1=[message to display]
function print-info() {

  echo "→ $1"
}

# Copy agent files to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-agents() {

  local dest_agents="$1/.github/agents"
  mkdir -p "${dest_agents}"

  print-info "Copying agent files to ${dest_agents}"
  find "${AGENTS_DIR}" -maxdepth 1 -name "*.md" -type f -exec cp {} "${dest_agents}/" \;
}

# Copy instruction files to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-instructions() {

  local dest_instructions="$1/.github/instructions"
  mkdir -p "${dest_instructions}"

  print-info "Copying instruction files to ${dest_instructions}"

  # Copy top-level instruction files
  find "${INSTRUCTIONS_DIR}" -maxdepth 1 -name "*.md" -type f -exec cp {} "${dest_instructions}/" \;

  # Copy include directory if it exists
  if [[ -d "${INSTRUCTIONS_DIR}/include" ]]; then
    mkdir -p "${dest_instructions}/include"
    find "${INSTRUCTIONS_DIR}/include" -name "*.md" -type f -exec cp {} "${dest_instructions}/include/" \;
  fi
}

# Copy prompt files to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-prompts() {

  local dest_prompts="$1/.github/prompts"
  mkdir -p "${dest_prompts}"

  print-info "Copying prompt files to ${dest_prompts}"
  find "${PROMPTS_DIR}" -maxdepth 1 -name "*.prompt.md" -type f -exec cp {} "${dest_prompts}/" \;
}

# Copy skills files to the destination (recursively including subdirectories).
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-skills() {

  local dest_skills="$1/.github/skills"

  print-info "Copying skills files to ${dest_skills}"
  # Use cp -R to preserve directory structure for nested skill packs
  cp -R "${SKILLS_DIR}" "$1/.github/"
}

# Copy copilot-instructions.md to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-copilot-instructions() {

  local dest="$1/.github"
  mkdir -p "${dest}"

  print-info "Copying copilot-instructions.md to ${dest}"
  cp "${COPILOT_INSTRUCTIONS}" "${dest}/"
}

# Copy constitution.md to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-constitution() {

  local dest="$1/.specify/memory"
  mkdir -p "${dest}"

  print-info "Copying constitution.md to ${dest}"
  cp "${CONSTITUTION}" "${dest}/"
}

# Copy adr-template.md to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-adr-template() {

  local dest="$1/docs/adr"
  mkdir -p "${dest}"

  print-info "Copying adr-template.md to ${dest}"
  cp "${ADR_TEMPLATE}" "${dest}/"
}

# Copy docs/.gitignore to the destination.
# Arguments (provided as function parameters):
#   $1=[destination directory path]
function copy-docs-gitignore() {

  local dest="$1/docs"
  mkdir -p "${dest}"

  print-info "Copying docs/.gitignore to ${dest}"
  cp "${DOCS_GITIGNORE}" "${dest}/"
}

# ==============================================================================

# Check if an argument is a truthy value.
# Arguments:
#   $1=[value to check]
function is-arg-true() {

  if [[ "$1" =~ ^(true|yes|y|on|1|TRUE|YES|Y|ON)$ ]]; then
    return 0
  else
    return 1
  fi
}

# ==============================================================================

is-arg-true "${VERBOSE:-false}" && set -x

main "$@"

exit 0
