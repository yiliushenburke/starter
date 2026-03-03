import json
import os
import subprocess


LOG_FILE = os.getenv("CLAUDE_LOG_FILE", "claude.log")


def get_modified_files():
    """Returns a list of modified and untracked files from git status."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = []
        for line in result.stdout.splitlines():
            if line.strip():
                files.append(line[3:].strip())
        return files
    except Exception:
        return []


def send_hook_decision(decision, reason=None):
    """Print the JSON response for a Claude Code hook.

    Args:
        decision: 'allow' or 'block'.
        reason: The reason for blocking (shown to the agent).
    """
    response = {"decision": decision}
    if reason:
        response["reason"] = reason
    print(json.dumps(response))
