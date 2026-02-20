#!/usr/bin/env python3
"""Simple updater that pulls the latest GitHub Release zip and switches installs."""

from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile
from pathlib import Path

# === Config ===
GITHUB_REPO = "Natpol50/AT-bot"
MAIN_ENTRY = "Files/AT_bot.py"      # entry file inside repo
INSTALL_DIR = Path(__file__).resolve().parent
VERSIONS_DIR = INSTALL_DIR / "versions"
CURRENT_LINK = INSTALL_DIR / "current"
STATE_FILE = INSTALL_DIR / ".updater_state.json"

API_LATEST = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_state(data: dict) -> None:
    STATE_FILE.write_text(json.dumps(data, indent=2))


def get_latest_release() -> dict:
    req = urllib.request.Request(
        API_LATEST,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "AT-bot-updater"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_asset(url: str, *, accept: str | None = None) -> bytes:
    headers = {"User-Agent": "AT-bot-updater"}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def extract_zip(data: bytes, dest: Path) -> None:
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        z.extractall(dest)


def switch_current(target: Path) -> None:
    if CURRENT_LINK.exists() or CURRENT_LINK.is_symlink():
        if CURRENT_LINK.is_symlink() or CURRENT_LINK.is_file():
            CURRENT_LINK.unlink()
        else:
            shutil.rmtree(CURRENT_LINK)

    try:
        os.symlink(target, CURRENT_LINK, target_is_directory=True)
    except (OSError, NotImplementedError):
        shutil.copytree(target, CURRENT_LINK)


def restart_bot() -> None:
    entry = CURRENT_LINK / MAIN_ENTRY
    if not entry.exists():
        print(f"[updater] entrypoint not found: {entry}")
        return
    print("[updater] restarting bot...")
    subprocess.Popen([sys.executable, str(entry)], cwd=str(CURRENT_LINK))
    sys.exit(0)


def main() -> int:
    if "YOUR_USER/YOUR_REPO" in GITHUB_REPO:
        print("[updater] please set GITHUB_REPO in updater.py")
        return 1

    VERSIONS_DIR.mkdir(exist_ok=True)

    state = load_state()
    latest = get_latest_release()
    tag = latest.get("tag_name") or latest.get("name")
    if not tag:
        print("[updater] could not determine latest release tag")
        return 1

    if state.get("last_tag") == tag:
        print(f"[updater] already on latest: {tag}")
        return 0

    assets = latest.get("assets", [])
    zip_asset = next((a for a in assets if a.get("name", "").lower().endswith(".zip")), None)
    if zip_asset:
        print(f"[updater] downloading {zip_asset['name']}...")
        data = download_asset(zip_asset["url"], accept="application/octet-stream")
    else:
        zip_url = latest.get("zipball_url")
        if not zip_url:
            print("[updater] no .zip asset or zipball_url found in release")
            return 1
        print("[updater] downloading source zip...")
        data = download_asset(zip_url)

    tmpdir = Path(tempfile.mkdtemp())
    try:
        extract_zip(data, tmpdir)
        candidates = [p for p in tmpdir.iterdir() if p.is_dir()]
        if not candidates:
            print("[updater] no folder found in zip")
            return 1

        new_version_dir = VERSIONS_DIR / tag
        if new_version_dir.exists():
            shutil.rmtree(new_version_dir)
        shutil.move(str(candidates[0]), str(new_version_dir))

        switch_current(new_version_dir)
        save_state({"last_tag": tag, "updated_at": time.time()})
        print(f"[updater] updated to {tag}")
        restart_bot()
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
