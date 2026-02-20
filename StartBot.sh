#!/usr/bin/env bash
set -euo pipefail

echo "Starting ATbot..."
echo

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  echo "Usage: ./StartBot.sh [OPTIONS]"
  echo "  --help        Show this help message"
  echo "  --version     Show version info for all source files"
  echo "  --update      Check GitHub Releases and update"
  echo "  --release     Run the latest release if present"
  echo "  --config=NAME Use bot config NAME (skip picker)"
  exit 0
fi

if [[ "${1:-}" == "--version" || "${1:-}" == "-v" ]]; then
  if [[ $# -gt 1 ]]; then
    echo "--version cannot be combined with other arguments."
    exit 1
  fi

  echo -e "\033[32m
 █████╗ ████████╗      ██████╗  ██████╗ ████████╗
██╔══██╗╚══██╔══╝      ██╔══██╗██╔═══██╗╚══██╔══╝
███████║   ██║  █████╗ ██████╔╝██║   ██║   ██║   
██╔══██║   ██║  ╚════╝ ██╔══██╗██║ 🦊██║   ██║   
██║  ██║   ██║         ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝   ╚═╝         ╚═════╝  ╚═════╝    ╚═╝  
\033[0m"

  python3 - <<'PY'
import ast
from pathlib import Path

FILES = [
    ("AT_bot.py",               "Files/AT_bot.py"),
    ("Dashboard.py",            "Files/Dashboard.py"),
    ("Tokenverif.py",           "Files/Tokenverif.py"),
    ("Lists.py",                "Files/Lists.py"),
    ("Displays.py",             "Files/Displays.py"),
    ("Dependency_installer.py", "Files/Dependency_installer.py"),
]

def extract(path):
    info = {"__version__": "?", "__last_revision__": "?", "__author__": "?"}
    try:
        tree = ast.parse(Path(path).read_text())
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in info:
                        try:
                            info[target.id] = str(ast.literal_eval(node.value))
                        except Exception:
                            pass
    except Exception:
        pass
    return info

W = 26
DIV = "\033[90m" + "─" * 74 + "\033[0m"
print(DIV)
print(f"  \033[1m{'File':<{W}}  {'Version':<10}  {'Last revision':<14}  Author\033[0m")
print(DIV)
for label, path in FILES:
    i = extract(path)
    if Path(path).exists():
        print(
            f"  \033[0m{label:<{W}}  \033[34m{i['__version__']:<10}\033[0m"
            f"  {i['__last_revision__']:<14}  {i['__author__']}"
        )
    else:
        print(f"  \033[90m{label:<{W}}  {'?':<10}  {'?':<14}  (file not found)\033[0m")
print(DIV)
print()
print("  Developed by \033[34mAsha the fox 🦊\033[0m")
print()
PY

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

# Launch the bot with any --config argument
if [[ "${1:-}" == --config=* ]]; then
  python3 "$BOT_ENTRY" "$1"
else
  python3 "$BOT_ENTRY"
fi

# If the bot crashes, don't close the window immediately
status=$?
if [[ $status -ne 0 ]]; then
  echo
  echo "The bot has crashed! Check the logs folder for details."
  read -r -p "Press Enter to exit..." _
fi
