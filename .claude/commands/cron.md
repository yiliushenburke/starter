---
createdAt: "2026-03-03T02:38:38.920Z"
modifiedAt: "2026-03-03T02:38:41.135Z"
---
Manage repetitive scheduled tasks using systemd user timers.

$ARGUMENTS

> **Note:** This command manages systemd user timers (Linux only). The cron sync script is at `.gemini/hooks/cron.py`.

Tasks are stored in `cron.toml` at the repository root:

```toml
[[tasks]]
name = "Daily Report"
schedule = "daily"  # systemd OnCalendar expression
prompt = "Generate a daily progress report and save it to journal/"
yolo = false
```

Your job:

1. Understand the intent (add, edit, list, or delete a task).

2. Modify `cron.toml` in the repository root. Create it if it doesn't exist.

3. The `schedule` field MUST use systemd `OnCalendar` syntax (e.g., 'minutely', 'hourly', '*-*-* 00:00:00').

4. After modifying `cron.toml`, synchronize with systemd by running: `python3 .gemini/hooks/cron.py`

5. The sync script creates/updates/removes `.service` and `.timer` files in `~/.config/systemd/user/` and reloads the daemon.

Ensure tasks have `name`, `schedule` (OnCalendar), `prompt`, and `yolo` (boolean) fields.

⠀