# Scheduled task plan

All times are Europe/London. Recurring tasks run in a fresh session each time. The prompts come from
`templates.md`, with `{DASHBOARD_URL}` and `{REPO_REF}` filled in at creation time. Those prompts are
stored privately on the account, never in this repo.

## Target schedule

| Task | When | Type | Model | Replaces |
|---|---|---|---|---|
| **CoS – Morning (staff sweep + brief)** | daily 04:13 | recurring | Opus | `Dashboard priorities` (retired). One session: the five DAILY sweeps, then the CoS MORNING section. Reuses a retired task that already had every connector attached. |
| **CoS – Wake / Home / Wind-down – <day>** | at the window times | one-shot, created by CoS – Evening | Opus | the coach's `Coach – Wake – …` one-shots |
| **Coach – Post: <session> – <day>** | key session end + 20 min | one-shot, created by CoS – Evening | Sonnet | same as now |
| **CoS – Evening** | daily 19:13 | recurring | Sonnet | `Event mode watcher` **and** `Coach check-in planner` (merged into one; the other is disabled) |
| **Staff – weekly reports** | Sun 19:37 | recurring | Opus | — (new) |
| **CoS – Weekly** (Sunday wind-down) | Sun 21:17 | recurring | Opus | `Weekly review prep` (update its prompt) |
| **CoS – Monthly** | 1st of the month, 19:43 | recurring | Opus | `Monthly direction check-in` (update its prompt) |

The Chief of Staff can push at most 3 times a day; the specialists' sweeps never push.

## Retire (already disabled; delete once the new set has run cleanly for a week)
the two disabled film tasks, the two disabled social tasks and the two old
per-weekday priorities tasks.

## Cutover order
1. ✅ Seed `agents/*` on the Dashboard (charters, personal watches, source links).
2. ✅ **CoS – Morning (staff sweep + brief)** live; `Dashboard priorities` disabled.
3. ✅ `Coach check-in planner` → **CoS – Evening**; `Event mode watcher` disabled.
4. Check the first evening's one-shot window tasks before they fire.

Note: a recurring task must carry its connectors (Calendar, Todoist, Gmail, Gregaria, AccuWeather,
Claude Code Remote, Drive). Tasks created from a session without connector grants get none, so reuse an
existing task or create it in the claude.ai scheduled tasks UI.
5. Update `Weekly review prep` → **CoS – Weekly**, create **Staff – weekly reports**, and update the monthly task.
