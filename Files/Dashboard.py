# -----------------------------------------------------------------------------
#  Dashboard.py
#  Copyright (c) 2026 Asha the Fox 🦊
#  All rights reserved.
#
#  This is the dashboard code for the ATbot project. 
#  Dashboard - Displays real-time monitoring and statistics for the AT-bot project.
#  Tracks translation metrics, API usage, server status, and system resources.
#
# -----------------------------------------------------------------------------
from __future__ import annotations

__author__ = "Asha Geyon (Natpol50)"
__version__ = 1.0
__last_revision__ = '2026-02-20'

import json
import os
import platform
import time
from dataclasses import dataclass, field
from pathlib import Path
from threading import RLock
from typing import Dict, List, Optional

import textual
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Static
import traceback

try:
    import psutil
except Exception:
    psutil = None

REFRESH_SECONDS = 2.0
MAX_EVENTS = 10


def _format_uptime(seconds: float) -> str:
    seconds = int(seconds)
    days, rem = divmod(seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, secs = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{secs}s")
    return " ".join(parts)


@dataclass
class DashboardState:
    start_time: float = field(default_factory=time.time)
    translations_total: int = 0
    translations_dpl: int = 0
    translations_gt: int = 0
    translations_errors: int = 0
    api_calls: Dict[str, int] = field(default_factory=lambda: {"deepl": 0, "google": 0})
    api_errors: int = 0
    servers: List[str] = field(default_factory=list)
    update_notice: Optional[str] = None
    last_events: List[dict] = field(default_factory=list)
    bot_version: Optional[str] = None
    config_file: Optional[str] = None
    bot_name: Optional[str] = None
    ascii_avatar: Optional[str] = None
    state_path: Optional[Path] = None
    _lock: RLock = field(default_factory=RLock, init=False, repr=False)

    def load_from_file(self) -> None:
        if not self.state_path or not self.state_path.exists():
            return
        try:
            data = json.loads(self.state_path.read_text())
        except Exception:
            return

        with self._lock:
            self.translations_total = int(data.get("translations_total", 0))
            self.translations_dpl = int(data.get("translations_dpl", 0))
            self.translations_gt = int(data.get("translations_gt", 0))
            self.translations_errors = int(data.get("translations_errors", 0))
            self.api_calls = dict(data.get("api_calls", {"deepl": 0, "google": 0}))
            self.api_errors = int(data.get("api_errors", 0))
            self.servers = list(data.get("servers", []))
            self.update_notice = data.get("update_notice")
            self.last_events = list(data.get("last_events", []))[-MAX_EVENTS:]
            self.bot_name = data.get("bot_name")
            self.ascii_avatar = data.get("ascii_avatar")

    def _save_to_file(self) -> None:
        if not self.state_path:
            return
        try:
            data = self.snapshot()
            self.state_path.write_text(json.dumps(data, indent=2))
        except Exception:
            pass

    def record_translation(self, translator: str, ok: bool) -> None:
        with self._lock:
            self.translations_total += 1
            if not ok:
                self.translations_errors += 1
                self._save_to_file()
                return
            if translator == "dpl":
                self.translations_dpl += 1
            elif translator == "gt":
                self.translations_gt += 1
            self._save_to_file()

    def record_api_call(self, provider: str, ok: bool) -> None:
        with self._lock:
            if provider in self.api_calls:
                self.api_calls[provider] += 1
            if not ok:
                self.api_errors += 1
            self._save_to_file()

    def set_servers(self, servers: List[str]) -> None:
        with self._lock:
            self.servers = list(servers)
            self._save_to_file()

    def set_update_notice(self, notice: Optional[str]) -> None:
        with self._lock:
            self.update_notice = notice
            self._save_to_file()

    def set_bot_info(self, version: Optional[str], config: Optional[str], bot_name: Optional[str] = None) -> None:
        with self._lock:
            self.bot_version = version
            self.config_file = config
            if bot_name is not None:
                self.bot_name = bot_name

    def set_avatar(self, ascii_art: str) -> None:
        with self._lock:
            self.ascii_avatar = ascii_art

    def add_event(self, message: str) -> None:
        with self._lock:
            self.last_events.append({"ts": time.time(), "msg": message})
            self.last_events = self.last_events[-MAX_EVENTS:]
            self._save_to_file()

    def snapshot(self) -> dict:
        with self._lock:
            return {
                "uptime": _format_uptime(time.time() - self.start_time),
                "translations_total": self.translations_total,
                "translations_dpl": self.translations_dpl,
                "translations_gt": self.translations_gt,
                "translations_errors": self.translations_errors,
                "api_calls": dict(self.api_calls),
                "api_errors": self.api_errors,
                "servers": list(self.servers),
                "update_notice": self.update_notice,
                "last_events": list(self.last_events),
                "bot_version": self.bot_version,
                "config_file": self.config_file,
                "bot_name": self.bot_name,
                "ascii_avatar": self.ascii_avatar,
            }

class ATBotDashboardApp(App):
    CSS = """
    Screen {
        layout: vertical;
        padding: 1;
    }

    #botinfo {
        border: round #5588aa;
        padding: 1;
        margin: 1;
        height: auto;
    }

    #stats, #api, #servers, #events, #system, #notice {
        border: round #666666;
        padding: 1;
        margin: 1;
        height: auto;
    }

    #footer-bar {
        dock: bottom;
        height: 1;
        background: $panel;
        padding: 0 1;
    }

    #footer-bindings {
        width: auto;
        content-align: left middle;
        color: $text;
    }

    #footer-credit {
        width: 1fr;
        content-align: right middle;
        color: $text-muted;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("t", "toggle_panels", "Toggle panels"),
    ]

    def __init__(self, state: DashboardState) -> None:
        super().__init__()
        self.state = state
        self.show_details = True

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(id="botinfo")
        yield Static(id="stats")
        yield Static(id="api")
        yield Static(id="servers")
        yield Static(id="events")
        yield Static(id="system")
        yield Static(id="notice")
        with Horizontal(id="footer-bar"):
            yield Static(
                "[b]q[/b] Quit  [b]t[/b] Toggle panels",
                id="footer-bindings",
            )
            yield Static(
                f"Running on [bold]Textual[/bold] v{textual.__version__}",
                id="footer-credit",
            )

    def on_mount(self) -> None:
        self.set_interval(REFRESH_SECONDS, self.refresh_view)
        self.refresh_view()

    def refresh_view(self) -> None:
        try:
            data = self.state.snapshot()

            # ── Bot info / avatar panel ─────────────────────────────────────
            ART_W, ART_H = 20, 10
            raw_art = data.get("ascii_avatar") or ""
            art_lines = raw_art.splitlines()
            # Pad / trim to ART_H rows
            art_lines = (art_lines + [""] * ART_H)[:ART_H]

            name    = data.get("bot_name") or "AT-bot"
            ver     = data.get("bot_version") or "?"
            cfg     = data.get("config_file") or "?"
            uptime  = data.get("uptime", "0s")
            info = [
                f"  {name}",
                f"  v{ver}   config: {cfg}",
                f"  uptime: {uptime}",
                "",
                "",
                "   Bot running on AT-bot Dashboard, [link=https://github.com/Natpol50/AT-bot]https://github.com/Natpol50/AT-bot[/link]",
            ]
            info = (info + [""] * ART_H)[:ART_H]

            botinfo_lines = []
            for a_line, i_line in zip(art_lines, info):
                botinfo_lines.append(f"{a_line:<{ART_W}}  {i_line}")
            self.query_one("#botinfo", Static).update("\n".join(botinfo_lines))

            self.query_one("#stats", Static).update(
                "[STATS]\n" + "\n".join(
                    [
                        f"Bot v{data.get('bot_version', 'unknown')} | Config: {data.get('config_file', 'unknown')}",
                        f"Uptime: {data['uptime']}",
                        f"Translations: {data['translations_total']} (DeepL {data['translations_dpl']}, Google {data['translations_gt']}, Errors {data['translations_errors']})",
                    ]
                )
            )

            self.query_one("#api", Static).update(
                "[API USAGE]\n" + "\n".join(
                    [
                        f"DeepL calls: {data['api_calls'].get('deepl', 0)}",
                        f"Google calls: {data['api_calls'].get('google', 0)}",
                        f"API errors: {data['api_errors']}",
                    ]
                )
            )

            server_lines = data["servers"]
            if server_lines:
                self.query_one("#servers", Static).update("[SERVERS]\n" + "\n".join(server_lines))
            else:
                self.query_one("#servers", Static).update("[SERVERS]\nNo servers detected yet.")

            events = data.get("last_events", [])
            if events:
                lines = []
                for event in events[-MAX_EVENTS:]:
                    ts = time.strftime("%H:%M:%S", time.localtime(event.get("ts", 0)))
                    lines.append(f"[{ts}] {event.get('msg', '')}")
                self.query_one("#events", Static).update("[LAST EVENTS]\n" + "\n".join(lines))
            else:
                self.query_one("#events", Static).update("[LAST EVENTS]\nWaiting for activity...")

            self.query_one("#system", Static).update("[SYSTEM]\n" + "\n".join(_system_snapshot()))

            if data["update_notice"]:
                self.query_one("#notice", Static).update("[UPDATE]\n" + data["update_notice"])
            else:
                self.query_one("#notice", Static).update("[UPDATE]\nNo updates detected.")
        except Exception:
            err = traceback.format_exc().strip().splitlines()[-1]
            self.query_one("#notice", Static).update(f"[UPDATE]\nDashboard error: {err}")

    def action_toggle_panels(self) -> None:
        self.show_details = not self.show_details
        for wid in ("#stats", "#api", "#servers", "#events", "#system", "#notice"):
            self.query_one(wid, Static).display = self.show_details


def _system_snapshot() -> List[str]:
    lines = [
        f"OS: {platform.system()} {platform.release()}",
        f"Python: {platform.python_version()}",
        f"PID: {os.getpid()}",
    ]

    if psutil:
        try:
            proc = psutil.Process()
            mem = proc.memory_info().rss / (1024 * 1024)
            cpu = proc.cpu_percent(interval=None)
            lines.append(f"Memory: {mem:.1f} MB")
            lines.append(f"CPU: {cpu:.1f}%")
        except Exception:
            pass

    return lines


def start_dashboard(state: DashboardState) -> None:
    app = ATBotDashboardApp(state)
    app.run()
