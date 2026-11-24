# Scheduled task plan

All times are Europe/London. Recurring tasks run in a fresh session each time. The prompts come from
`templates.md`, with `{DASHBOARD_URL}` and `{REPO_REF}` filled in at creation time. Those prompts are
stored privately on the account, never in this repo.

## Target schedule

| Task | When | Type | Model | Replaces |
|---|---|---|---|---|
| **Staff – daily sweep** (the five coaches) | daily 04:13 | recurring | **Sonnet** | — (reuses a retired film task that already had every connector) |
| **Ava – Morning** | daily 04:43 | recurring | **Opus** | `Dashboard priorities` (retired) |
| **Ava – Wake / Home / Wind-down** | fixed times per weekday, set from the usual calendar | recurring (7 tasks, reusing retired tasks so connectors stay) | Opus | the coach's `Coach – Wake – …` one-shots; key-session debriefs fold into Home / Wind-down |
| **Ava – Evening** | daily 19:13 | recurring | Opus | `Event mode watcher` **and** `Coach check-in planner` (merged into one; the other is disabled) |
| **Staff – weekly reports** | Sun 19:37 | recurring | Sonnet | — (new) |
| **CoS – Weekly** (Sunday wind-down) | Sun 21:17 | recurring | Opus | `Weekly review prep` (update its prompt) |
| **CoS – Monthly** | 1st of the month, 19:43 | recurring | Opus | `Monthly direction check-in` (update its prompt) |

Model rule: Ava (the Chief of Staff) runs on Opus; the five coaches run on Sonnet. Ava can push at most 3 times a day; the coaches' sweeps never push. The HQ chat on the Dashboard asks for Opus too.

## Retire (already disabled; delete once the new set has run cleanly for a week)
the two disabled film tasks, the two disabled social tasks and the two old
per-weekday priorities tasks.

## Cutover order
1. ✅ Seed `agents/*` on the Dashboard (charters, personal watches, source links).
2. ✅ **CoS – Morning (staff sweep + brief)** live; `Dashboard priorities` disabled.
3. ✅ `Coach check-in planner` → **CoS – Evening**; `Event mode watcher` disabled.
4. ✅ First day checked (24 Nov): 3/3 messages, no agent errors, approvals carried out.

Note: a recurring task must carry its connectors (Calendar, Todoist, Gmail, Gregaria, AccuWeather,
Claude Code Remote, Drive). Tasks created from a session without connector grants get none, so reuse an
existing task or create it in the claude.ai scheduled tasks UI.
5. ✅ `Weekly review prep` → **Ava – Weekly review** (Sun 21:17), **Staff – weekly reports** (Sun 19:37, reusing a retired task), monthly task → **Ava – Monthly check-in**.

## Why fixed times
Scheduled runs are refused when they try to create scheduled tasks, so nothing is created on the fly. Window times are fixed recurring tasks; change them from an interactive session.
