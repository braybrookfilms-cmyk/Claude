# Scheduled task plan

All times are Europe/London. Recurring tasks run in a fresh session each time. The prompts come from
`templates.md`, with `{DASHBOARD_URL}` and `{REPO_REF}` filled in at creation time. Those prompts are
stored privately on the account, never in this repo.

## Target schedule

| Task | When | Type | Model | Replaces |
|---|---|---|---|---|
| **Staff – daily sweep** | daily 04:13 | recurring | Sonnet | — (new) |
| **CoS – Morning** | daily 04:45 | recurring | Sonnet | `Dashboard priorities` (update its prompt to keep its history) |
| **CoS – Wake / Home / Wind-down – <day>** | at the window times | one-shot, created by CoS – Evening | Opus | the coach's `Coach – Wake – …` one-shots |
| **Coach – Post: <session> – <day>** | key session end + 20 min | one-shot, created by CoS – Evening | Sonnet | same as now |
| **CoS – Evening** | daily 19:13 | recurring | Sonnet | `Event mode watcher` **and** `Coach check-in planner` (merged into one; the other is disabled) |
| **Staff – weekly reports** | Sun 19:37 | recurring | Opus | — (new) |
| **CoS – Weekly** (Sunday wind-down) | Sun 21:17 | recurring | Opus | `Weekly review prep` (update its prompt) |
| **CoS – Monthly** | 1st of the month, 19:43 | recurring | Opus | `Monthly direction check-in` (update its prompt) |

The Chief of Staff can push at most 3 times a day; the specialists' sweeps never push.

## Retire (already disabled; delete once the new set has run cleanly for a week)
`Film – shoot briefs`, `Film – Sunday production meeting`, `Oli Runs social – daily check`,
`Oli Runs social – weekly batch`, `Dashboard priorities – Sun`, `Dashboard priorities – Mon/Tue/Wed/Sat`.

## Cutover order
1. Seed `agents/*` on the Dashboard (charters, personal watches, source links).
2. Update `Dashboard priorities` → **CoS – Morning**, and create **Staff – daily sweep**.
3. Update `Coach check-in planner` → **CoS – Evening**, and disable `Event mode watcher`.
4. Check the first evening's one-shot window tasks before they fire.
5. Update `Weekly review prep` → **CoS – Weekly**, create **Staff – weekly reports**, and update the monthly task.
