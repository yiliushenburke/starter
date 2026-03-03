#!/usr/bin/env python3
"""Stop hook: enforce journal entries for significant changes.

Blocks the agent from stopping if there are uncommitted changes
but no entry in today's journal file.
"""
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils


def main():
    try:
        modified_files = utils.get_modified_files()

        today = datetime.now().strftime("%Y-%m-%d")
        journal_file = f"journal/{today}.md"

        significant_changes = [f for f in modified_files if f != journal_file]
        journal_updated = journal_file in modified_files

        if significant_changes and not journal_updated:
            utils.send_hook_decision(
                "block",
                reason=(
                    f"Add a one-line entry to {journal_file} "
                    "describing the changes you just made. "
                    "Do not stop until this file is updated."
                ),
            )
        else:
            utils.send_hook_decision("allow")

    except Exception:
        utils.send_hook_decision("allow")


if __name__ == "__main__":
    main()
