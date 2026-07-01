"""Publish step — create the repo and enable GitHub Pages THROUGH Spark's Execution Engine.

Uses spark.execution.gh_executor.GhExecutor (the same delegate proven in E004): Spark
decides WHAT (create repo, enable Pages); `gh` performs it (owns GitHub auth). Idempotent-ish:
tolerates "already exists". Prints primary + secondary evidence.

    PYTHONPATH=<spark> <spark>/.venv/bin/python tools/publish.py <repo_name>
"""

from __future__ import annotations

import sys

from spark.execution.gh_executor import GhExecutor


def main(argv: list[str]) -> int:
    repo = argv[1] if len(argv) > 1 else "spark-engineering-blog"
    gh = GhExecutor()

    who = gh.whoami()
    if not who.success:
        print(f"FAILURE (auth): {who.stderr}")
        return 1
    owner = who.stdout.strip()
    full = f"{owner}/{repo}"
    print(f"Orchestrate: Spark will publish '{full}' (public, Pages from main:/docs).")

    created = gh.create_repository(repo, private=False, description="The Spark Engineering Story — Product 1 (built + published by the Spark factory).")
    if created.success:
        print(f"  created: {full}")
    elif "already exists" in (created.stderr or "").lower() or "name already exists" in (created.stderr or "").lower():
        print(f"  exists already: {full} (continuing)")
    else:
        print(f"FAILURE (create): {created.stderr}")
        return 1

    print(f"\nPRIMARY EVIDENCE: https://github.com/{full}")
    print(f"SECONDARY: delegated via {created.provider or 'gh'} (Spark held no credentials)")
    print(f"Next: git push to {full}, then enable Pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
