#!/usr/bin/env python3
"""Textual-based TUI dashboard for ATbot."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from threading import Lock, Thread
from typing import Dict, List, Optional

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static


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
    _lock: Lock = field(default_factory=Lock, init=False, repr=False)

    def record_translation(self, translator: str, ok: bool) -> None:
        with self._lock:
            self.translations_total += 1
            if not ok:
                self.translations_errors += 1
                return
            if translator == "dpl":
                self.translations_dpl += 1
            elif translator == "gt":
                self.translations_gt += 1

    def record_api_call(self, provider: str, ok: bool) -> None:
        with self._lock:
            if provider in self.api_calls:
                self.api_calls[provider] += 1
            if not ok:
                self.api_errors += 1

    def set_servers(self, servers: List[str]) -> None:
        with self._lock:
            self.servers = list(servers)

    def set_update_notice(self, notice: Optional[str]) -> None:
        with self._lock:
            self.update_notice = notice

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
            }


class DashboardApp(App):
    CSS = """
    Screen {
        layout: vertical;
        padding: 1;
    }

    #stats, #servers, #notice {
        border: round #666666;
        padding: 1;
        margin: 1;
    }
    """

    def __init__(self, state: DashboardState) -> None:
        super().__init__()
        self.state = state
        self.stats = Static(id="stats")
        self.servers = Static(id="servers")
        self.notice = Static(id="notice")

    def compose(self) -> ComposeResult:
        yield Header()
        yield self.stats
        yield self.servers
        yield self.notice
        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(1.0, self.refresh_view)
        self.refresh_view()

    def refresh_view(self) -> None:
        data = self.state.snapshot()
        self.stats.update(
            "\n".join(
                [
                    f"Uptime: {data['uptime']}",
                    f"Translations: {data['translations_total']} (DeepL {data['translations_dpl']}, Google {data['translations_gt']}, Errors {data['translations_errors']})",
                    f"API calls: DeepL {data['api_calls'].get('deepl', 0)}, Google {data['api_calls'].get('google', 0)}, Errors {data['api_errors']}",
                ]
            )
        )

        server_lines = data["servers"] or ["No servers detected yet."]
        self.servers.update("Servers:\n" + "\n".join(server_lines))

        if data["update_notice"]:
            self.notice.update("Update:\n" + data["update_notice"])
        else:
            self.notice.update("Update:\nNo updates detected.")


def start_dashboard(state: DashboardState) -> None:
    def runner() -> None:
        app = DashboardApp(state)
        app.run()

    thread = Thread(target=runner, daemon=True)
    thread.start()
