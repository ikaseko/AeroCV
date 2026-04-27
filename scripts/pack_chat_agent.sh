#!/usr/bin/env bash
# Packs AeroCV assets into a ZIP for chat/cloud GPT agents.
# Builds chat_agent_output/aerocv-chat-agent.zip containing:
# - typst binary (from PATH or local)
# - metadata.md, previews.zip, per-template zips
# - system_prompt.md (SYSTEM_PROMPT_TYPST.md)
#
# Usage: ./scripts/pack_chat_agent.sh [--typst /path/to/typst]

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$ROOT/chat_agent_output"
TYPST_PATH=""

for arg in "$@"; do
    case $arg in
        --typst=*) TYPST_PATH="${arg#*=}" ;;
        --typst)   shift; TYPST_PATH="$1" ;;
    esac
done

echo "=== AeroCV Chat Agent Packager ==="

# Step 1: Find typst binary
if [ -n "$TYPST_PATH" ] && [ -f "$TYPST_PATH" ]; then
    typst="$TYPST_PATH"
elif [ -f "$ROOT/typst" ]; then
    typst="$ROOT/typst"
elif command -v typst &>/dev/null; then
    typst="$(command -v typst)"
else
    echo "ERROR: typst binary not found."
    echo "Install from https://github.com/typst/typst/releases or pass --typst /path/to/typst"
    exit 1
fi
echo "Using typst: $typst"

# Step 2: Rebuild agent_output/
echo ""
echo "--- Running pack_per_template.py ---"
python3 "$ROOT/scripts/pack_per_template.py"

# Step 3: Create output directory
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Step 4: Build the combined zip
ZIP_PATH="$OUTPUT_DIR/aerocv-chat-agent.zip"
echo ""
echo "--- Building aerocv-chat-agent.zip ---"

cd "$ROOT"

# Create zip with typst binary + agent_output files + system prompt
zip -j -9 "$ZIP_PATH" "$typst"

if [ -d "$ROOT/agent_output" ]; then
    cd "$ROOT/agent_output"
    zip -j -9 "$ZIP_PATH" *
fi

cd "$ROOT"
zip -j -9 "$ZIP_PATH" SYSTEM_PROMPT_TYPST.md

# Rename SYSTEM_PROMPT_TYPST.md -> system_prompt.md inside zip
# (zip -j uses the filename as-is, so we copy with the right name first)
cp SYSTEM_PROMPT_TYPST.md /tmp/system_prompt.md
zip -j -9 "$ZIP_PATH" /tmp/system_prompt.md
# Remove the duplicate entry with original name
zip -d "$ZIP_PATH" "SYSTEM_PROMPT_TYPST.md" 2>/dev/null || true
rm -f /tmp/system_prompt.md

SIZE_MB=$(du -m "$ZIP_PATH" | cut -f1)
echo ""
echo "Done: $ZIP_PATH (${SIZE_MB} MB)"
