#!/usr/bin/env python3
"""
Archive GitHub repository traffic metrics.

GitHub exposes repository traffic for the last 14 days only. Run this script
daily to keep a local long-term history of views, clones, referrers, and
popular paths.

Requirements:
  - GitHub CLI (`gh`) installed and authenticated
  - Push/admin access to the repository

Usage:
  python scripts/github_traffic_monitor.py --repo tyilmaz23/DRLAlgoMapfree
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REPO = "tyilmaz23/DRLAlgoMapfree"
DEFAULT_OUTPUT = Path("analytics/github_traffic_history.json")


def find_gh() -> str:
    gh = shutil.which("gh")
    if gh:
        return gh

    candidates = [
        r"C:\Program Files\GitHub CLI\gh.exe",
        r"C:\Users\mekatronik\AppData\Local\Programs\GitHub CLI\gh.exe",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate

    raise SystemExit("GitHub CLI was not found. Install gh and run `gh auth login`.")


def gh_api(gh: str, endpoint: str) -> Any:
    result = subprocess.run(
        [gh, "api", endpoint],
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def load_history(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_history(path: Path, history: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=DEFAULT_REPO, help="Repository in owner/name format")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="JSON history path")
    args = parser.parse_args()

    gh = find_gh()
    repo = args.repo.strip("/")
    output = Path(args.output)

    snapshot = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "repo": repo,
        "views": gh_api(gh, f"/repos/{repo}/traffic/views"),
        "clones": gh_api(gh, f"/repos/{repo}/traffic/clones"),
        "referrers": gh_api(gh, f"/repos/{repo}/traffic/popular/referrers"),
        "popular_paths": gh_api(gh, f"/repos/{repo}/traffic/popular/paths"),
    }

    history = load_history(output)
    history.append(snapshot)
    save_history(output, history)

    print(f"Saved GitHub traffic snapshot to {output}")
    print(f"Views: {snapshot['views'].get('count', 0)} total, {snapshot['views'].get('uniques', 0)} unique")
    print(f"Clones: {snapshot['clones'].get('count', 0)} total, {snapshot['clones'].get('uniques', 0)} unique")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
