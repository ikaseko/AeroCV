#!/usr/bin/env bash
# Downloads typst binary for the current platform.
# Skips if typst is already available in PATH or project root.
#
# Usage: ./scripts/setup.sh [--version 0.12.0]

set -euo pipefail
VERSION="${2:-0.12.0}"

if command -v typst &>/dev/null || [ -f ./typst ]; then
    echo "typst already available."
    typst --version 2>/dev/null || ./typst --version 2>/dev/null
    exit 0
fi

OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"
case "$OS" in
    linux)  OS="linux" ;;
    darwin) OS="macos" ;;
    *)      echo "Unsupported OS: $OS"; exit 1 ;;
esac
case "$ARCH" in
    x86_64|amd64)  ARCH="x86_64" ;;
    aarch64|arm64) ARCH="aarch64" ;;
    *)             echo "Unsupported arch: $ARCH"; exit 1 ;;
esac

FILE="typst-${VERSION}-${OS}-${ARCH}.tar.xz"
URL="https://github.com/typst/typst/releases/download/v${VERSION}/${FILE}"

echo "Downloading typst v${VERSION} for ${OS}-${ARCH}..."
echo "URL: $URL"

TMPDIR=$(mktemp -d)
curl -fSL -o "${TMPDIR}/${FILE}" "$URL"

echo "Extracting..."
tar -xf "${TMPDIR}/${FILE}" -C "${TMPDIR}"

TYPST_BIN=$(find "${TMPDIR}" -name typst -type f | head -1)
if [ -z "$TYPST_BIN" ]; then
    echo "ERROR: typst binary not found in archive"
    exit 1
fi

cp "$TYPST_BIN" ./typst
chmod +x ./typst

rm -rf "${TMPDIR}"

echo ""
echo "typst v${VERSION} installed successfully."
./typst --version
