#!/usr/bin/env bash
#
# LinkedIn AI Orchestrator - 1-Click Installer & Restorer
# Restores the entire LinkedIn automation and skill into Antigravity
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="$HOME/.gemini/antigravity/bin"
SKILLS_DIR="$HOME/.gemini/config/skills/linkedin-orchestrator"
RULES_FILE="$HOME/.gemini/GEMINI.md"

echo "============================================="
echo "  LinkedIn AI Orchestrator - Setup & Restore"
echo "============================================="

# 1. Ensure bin directories exist
mkdir -p "$BIN_DIR" "$HOME/.local/bin" "$SKILLS_DIR"

# 2. Symlink CLI tools
ln -sf "$SCRIPT_DIR/scripts/post_linkedin.py" "$BIN_DIR/linkedin-post"
ln -sf "$SCRIPT_DIR/scripts/post_linkedin.py" "$HOME/.local/bin/linkedin-post"
ln -sf "$SCRIPT_DIR/scripts/find-skill.py" "$BIN_DIR/find-skill"
ln -sf "$SCRIPT_DIR/scripts/find-skill.py" "$HOME/.local/bin/find-skill"
chmod +x "$SCRIPT_DIR"/scripts/*.py

# 3. Install Antigravity Skill
cp "$SCRIPT_DIR/skills/linkedin-orchestrator/SKILL.md" "$SKILLS_DIR/SKILL.md"

echo "✅ Installed CLI tools to: $BIN_DIR/linkedin-post"
echo "✅ Installed Skill to: $SKILLS_DIR/SKILL.md"

# 4. Check Authentication
AUTH_FILE="$HOME/.gemini/config/linkedin_auth.json"
if [ -f "$AUTH_FILE" ]; then
    echo "✅ Found existing LinkedIn credentials at $AUTH_FILE"
else
    echo "⚠️  LinkedIn is not authenticated yet."
    echo "Run: linkedin-post --setup"
fi

echo ""
echo "🎉 Setup complete! You can now use the linkedin-orchestrator skill in Antigravity."
