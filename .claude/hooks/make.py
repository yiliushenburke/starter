#!/usr/bin/env python3
"""Stop hook: run 'make' validation before the agent finishes.

Blocks the agent from stopping if lint or tests fail,
forcing it to fix the issues first.
"""
import subprocess
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils


def main():
    try:
        result = subprocess.run(
            ["make"],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            output = (result.stdout + "\n" + result.stderr).strip()
            utils.send_hook_decision(
                "block",
                reason=(
                    f"Validation failed (make returned {result.returncode}).\n"
                    "Fix the broken tests or linting issues.\n"
                    f"Output:\n```\n{output}\n```\n"
                    "Fix these issues and ensure 'make' passes before stopping."
                ),
            )
        else:
            utils.send_hook_decision("allow")

    except FileNotFoundError:
        # No Makefile — nothing to validate
        utils.send_hook_decision("allow")
    except Exception:
        utils.send_hook_decision("allow")


if __name__ == "__main__":
    main()
