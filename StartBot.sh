#!/usr/bin/env bash
set -euo pipefail

echo "Starting ATbot..."
echo

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  echo "Usage: ./StartBot.sh [--update] [--release]"
  echo "  --update   Check GitHub Releases and update"
  echo "  --release  Run the latest release if present"
  exit 0
fi

# Check if Python is installed
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is not installed or not in PATH!"
  echo "Please install Python 3.8 or higher from https://www.python.org/downloads/"
  exit 1
fi

# Optional updater
if [[ "${1:-}" == "--update" ]]; then
  if [[ ! -f "updater.py" ]]; then
    echo "Error: updater.py not found!"
    exit 1
  fi
  python3 "updater.py" || exit $?
fi

# Pick dev vs release based on version when both exist
DEV_ENTRY="Files/AT_bot.py"
REL_ENTRY="current/Files/AT_bot.py"

if [[ "${1:-}" == "--release" && -f "$REL_ENTRY" ]]; then
  BOT_ENTRY="$REL_ENTRY"
elif [[ -f "$DEV_ENTRY" && -f "$REL_ENTRY" ]]; then
  BOT_ENTRY=$(python3 - <<'PY'
import ast
import re
from pathlib import Path

def parse_version(path: str) -> tuple:
    try:
        tree = ast.parse(Path(path).read_text())
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "__version__":
                        value = ast.literal_eval(node.value)
                        parts = re.findall(r"\d+", str(value))
                        return tuple(int(p) for p in parts) if parts else (0,)
    except Exception:
        return (0,)
    return (0,)

dev = "Files/AT_bot.py"
rel = "current/Files/AT_bot.py"
print(dev if parse_version(dev) >= parse_version(rel) else rel)
PY
  )
elif [[ -f "$DEV_ENTRY" ]]; then
  BOT_ENTRY="$DEV_ENTRY"
elif [[ -f "$REL_ENTRY" ]]; then
  BOT_ENTRY="$REL_ENTRY"
else
  echo "Error: Files/AT_bot.py not found!"
  echo "Please make sure you're running this script from the project root."
  exit 1
fi

# Launch the bot
python3 "$BOT_ENTRY"

# If the bot crashes, don't close the window immediately
status=$?
if [[ $status -ne 0 ]]; then
  echo
  echo "The bot has crashed! Check the logs folder for details."
  read -r -p "Press Enter to exit..." _
fi
