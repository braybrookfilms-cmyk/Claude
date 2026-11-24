# Data model (Dashboard database)

All agents read and write the Dashboard's database with the `ArtifactData` tool. The Dashboard URL is
passed in by each scheduled task prompt. Rules:
- Read a document before writing it, and pin every write with `if_version`.
- Use `batch` for more than two writes.
- Dates are `YYYY-MM-DD` and times are `HH:MM`, both Europe/London.
- `agent` ids: `cos`, `run`, `life`, `money`, `biz`, `growth`.

## Existing collections (kept as they are)

| Collection | Owner | Use |
|---|---|---|
| `house_rules/*` | principal | Standing decisions. Everyone reads them; **scheduled runs never write them**. |
| `board/today` | cos | Today's top 3 `{date, priorities[{done,text,todoistId?}], note}` |
| `board/mode` | cos | `{mode: normal\|event\|trip\|reentry, label, from, until, set: auto\|manual, updated}` |
| `coach_radar`, `coach_checkins`, `checkins` | run | Running coach's own working notes and check-in links |
| `ticks`, `routine_skips`, `fuel_*` | life | Habit ticks, skips, food and hydration logs |
| `portfolio`, `portfolio_history` | money | Weekly portfolio numbers |
| `monthly_checkins/YYYY-MM` | growth | Monthly start/stop answers |
| `countdowns/*` | cos | Key dates |

## New collections

### `agents/<agent>`: charter and status (one doc per agent)
```json
{
  "agent": "money",
  "name": "Financial advisor",
  "mission": "one line",
  "scope": ["what it covers"],
  "watches": [{"id": "numbers-missing", "rule": "plain-English trigger", "severity": "med"}],
  "sources": {"artifact_urls": [], "notes": "where its data lives"},
  "cadence": "daily sweep + Sunday report",
  "rag": "green|amber|red",
  "headline": "one line on how this area is going",
  "last_run": "2026-11-24T04:20",
  "last_status": "ok|warn|error",
  "last_error": ""
}
```
Personal details (race dates, names, account labels, thresholds) belong here and in `goals`, not in the repo.

### `goals/<agent>-<slug>`
```json
{
  "agent": "run", "quarter": "2026Q4", "title": "Hyrox ready",
  "outcome": {"measure": "race finish time", "target": "…", "current": "…"},
  "lead": {"measure": "key sessions hit per week", "target": 2, "current": 2},
  "status": "draft|active|done|dropped", "review_by": "2027-01-31", "updated": "…"
}
```
Agents may write goals with `status: "draft"`. A goal becomes `active` only once the principal agrees to it.

### `signals/<YYYYMMDD>-<agent>-<slug>`
```json
{
  "agent": "life", "kind": "alert|risk|opportunity|win|info",
  "severity": "low|med|high|urgent",
  "horizon": "today|week|month",
  "title": "short", "why": "one or two lines with the evidence",
  "proposed_action": "what to do about it, or empty",
  "action_id": "optional link to actions/*",
  "watch": "the watch id that fired, if any",
  "status": "open|surfaced|acted|dismissed|expired",
  "until": "YYYY-MM-DD", "created": "…", "updated": "…"
}
```
**Deduplicating:** before writing, query open signals with the same `agent` and `watch` (or the same slug).
If one exists, update its `why`, `severity` and `until` instead of creating another.

### `actions/<YYYYMMDD>-<agent>-<slug>`: the approval queue
```json
{
  "agent": "biz", "title": "Email the club secretary to book the chat",
  "type": "email|calendar|todoist|training|other",
  "payload": {"exact": "the precise change: recipients, subject and body; or event fields; or task fields"},
  "why": "one line",
  "status": "pending|approved|declined|snoozed|done|failed|expired",
  "snooze_until": "", "expires": "YYYY-MM-DD",
  "created": "…", "decided": "…", "executed": "…", "result": ""
}
```

Actions he asks for directly in the Dashboard chat are created already `approved`, with
`source: "dashboard-chat"`.

### `ava_chat/<epoch ms>`: the HQ chat with Ava
`{"role": "user|assistant", "text": "…", "t": 1764000000000, "did": ["what her tools changed"]}`

### `rnd/<YYYYMMDD>-<slug>`: R&D the Chief of Staff directs
```json
{
  "from": "cos", "to": "biz", "ask": "Compare UK coaching insurance options",
  "why": "…", "due": "YYYY-MM-DD",
  "status": "open|doing|done", "result": "summary", "link": "optional doc link"
}
```

### `reports/<agent>-<YYYY-Www>`: weekly report from each specialist
```json
{
  "agent": "money", "week": "2026-W48", "rag": "green|amber|red",
  "last_week": ["…"], "next_week": ["…"], "goal_progress": [{"goal": "id", "lead": "…", "outcome": "…"}],
  "asks": ["questions or numbers needed from the principal"], "created": "…"
}
```

### `briefs/<YYYY-MM-DD>`: Chief of Staff daily brief (what the HQ tab shows)
```json
{
  "date": "…", "headline": "one line",
  "agents": {"run": {"rag": "green", "line": "…"}, "life": {}, "money": {}, "biz": {}, "growth": {}},
  "windows": {
    "wake": {"at": "07:00", "sent": false, "summary": ""},
    "home": {"at": "18:10", "sent": false, "summary": ""},
    "winddown": {"at": "21:30", "sent": false, "summary": ""}
  },
  "pending_actions": ["action ids"], "updated": "…"
}
```

### `pings/<YYYY-MM-DD>`: ping budget ledger
```json
{"date": "…", "count": 1, "sent": [{"at": "07:02", "window": "wake", "by": "cos", "summary": "…"}]}
```

### `biz_state/summary`: Coach Quest summary for the Dashboard (biz)
A copy of the quest tracker's progress, written by the business coach on every run, because the page can't
read the tracker's own database. Shape and rules: `business-coach` skill, "Dashboard summary".

### `growth_log/<YYYY-MM-DD>`: make sessions (growth)
```json
{"date": "2026-11-24", "make": true, "t": 1764000000000, "src": "dashboard|dashboard-chat|ava"}
```
One doc per day he did his make session. Deleting it un-ticks the day.

### `interviews/<agent>`: intake interview state
```json
{"agent": "growth", "status": "not_started|in_progress|done", "answers": {}, "outcome": "…", "updated": "…"}
```
