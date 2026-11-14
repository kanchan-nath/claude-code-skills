#!/usr/bin/env bash
# Claude Code & AI Agent Skills Installer
# Repo: https://github.com/kanchan-nath/claude-code-skills

set -euo pipefail

REPO_RAW_URL="https://raw.githubusercontent.com/kanchan-nath/claude-code-skills/main"
REPO_GIT_URL="https://github.com/kanchan-nath/claude-code-skills.git"

AVAILABLE_SKILLS=(
  "cold-email"
  "content-ideas"
  "create-linkedin-post"
  "dsa"
  "hashnode"
  "job"
  "linkedin-humanizer"
  "linkedin-orchestrator"
  "linkedin-post-image"
  "motion-prompt-director"
  "referral"
  "seo"
  "shorts-script-writer"
  "sparke-codestyle"
)

usage() {
  cat <<EOF
Usage:
  install.sh [skill-name] [options]
  install.sh --all [options]
  install.sh --list

Options:
  --target <claude|antigravity|project|custom>
                        Target environment:
                          claude (default) -> ~/.claude/skills/
                          antigravity      -> ~/.gemini/config/skills/
                          project          -> ./.claude/skills/
  --dir <path>          Custom target directory
  --list                List all available skills
  --all                 Install all available skills
  -h, --help            Show this help message

Examples:
  bash install.sh cold-email
  bash install.sh create-linkedin-post --target antigravity
  bash install.sh --all --target claude
  curl -fsSL ${REPO_RAW_URL}/install.sh | bash -s cold-email
EOF
}

TARGET="claude"
TARGET_DIR=""
SKILL_TO_INSTALL=""
INSTALL_ALL=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --list)
      echo "Available Skills in kanchan-nath/claude-code-skills:"
      for s in "${AVAILABLE_SKILLS[@]}"; do
        echo "  - $s"
      done
      exit 0
      ;;
    --all)
      INSTALL_ALL=true
      shift
      ;;
    --target)
      TARGET="$2"
      shift 2
      ;;
    --dir)
      TARGET_DIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      if [[ -z "$SKILL_TO_INSTALL" ]]; then
        SKILL_TO_INSTALL="$1"
      fi
      shift
      ;;
  esac
done

# Resolve destination directory
if [[ -z "$TARGET_DIR" ]]; then
  case "$TARGET" in
    claude)
      TARGET_DIR="${HOME}/.claude/skills"
      ;;
    antigravity|gemini)
      TARGET_DIR="${HOME}/.gemini/config/skills"
      ;;
    project)
      TARGET_DIR="./.claude/skills"
      ;;
    *)
      echo "Unknown target: $TARGET. Choose claude, antigravity, project, or use --dir <path>." >&2
      exit 1
      ;;
  esac
fi

mkdir -p "$TARGET_DIR"

install_single_skill() {
  local skill="$1"
  local dest="${TARGET_DIR}/${skill}"
  echo "Installing skill '${skill}' into ${dest}..."

  # Check if local repository
  local script_dir
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd || echo "")"
  if [[ -n "$script_dir" && -d "${script_dir}/skills/${skill}" ]]; then
    mkdir -p "$dest"
    cp -R "${script_dir}/skills/${skill}/"* "$dest/"
    echo "✓ '${skill}' installed successfully from local workspace."
    return 0
  fi

  # Remote installation via git sparse-checkout or clone
  local tmp_dir
  tmp_dir=$(mktemp -d)
  trap 'rm -rf "$tmp_dir"' EXIT

  git clone --depth 1 --filter=blob:none --sparse "$REPO_GIT_URL" "$tmp_dir/repo" >/dev/null 2>&1 || {
    # Fallback to shallow clone if sparse not supported
    git clone --depth 1 "$REPO_GIT_URL" "$tmp_dir/repo" >/dev/null 2>&1
  }

  if [[ -d "$tmp_dir/repo/skills/${skill}" ]]; then
    mkdir -p "$dest"
    cp -R "$tmp_dir/repo/skills/${skill}/"* "$dest/"
    echo "✓ '${skill}' installed successfully."
  else
    echo "Error: Skill '${skill}' not found in repository." >&2
    exit 1
  fi
}

if [[ "$INSTALL_ALL" = true ]]; then
  echo "Installing all ${#AVAILABLE_SKILLS[@]} skills to ${TARGET_DIR}..."
  for s in "${AVAILABLE_SKILLS[@]}"; do
    install_single_skill "$s"
  done
  echo "✓ All skills successfully installed."
  exit 0
fi

if [[ -z "$SKILL_TO_INSTALL" ]]; then
  echo "Error: No skill specified." >&2
  usage
  exit 1
fi

install_single_skill "$SKILL_TO_INSTALL"
