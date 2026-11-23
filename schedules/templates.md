# Prompt templates

Placeholders: `{DASHBOARD_URL}` (the Dashboard artifact), `{REPO_REF}` (the branch holding these skills,
e.g. `main`), `{DAY}` (e.g. `Tue 24 Nov`), `{DATE}` (`YYYY-MM-DD`), `{WINDOW}` (`wake|home|winddown`).

Every template starts with the PREAMBLE.

## PREAMBLE
```
You are part of a Chief of Staff agent team. The Dashboard is {DASHBOARD_URL}; its database is reached
with the ArtifactData tool (load it via ToolSearch). Time zone Europe/London. Skills: load them with the
Skill tool. If a skill named below isn't listed, read .claude/skills/<name>/SKILL.md (and
contracts/policy.md, contracts/data-model.md) from GitHub repo braybrookfilms-cmyk/Claude at ref
{REPO_REF} with the GitHub get_file_contents tool, and follow it the same way. Never publish anything.
```

## Staff – daily sweep
```
{PREAMBLE}
Run type: DAILY. Load staff-protocol. Then, one after another, load and run the DAILY section of:
running-coach, lifestyle-coach, financial-advisor, business-coach, personal-development-coach.
Each agent writes its own signals, actions and agents/<id> status. Send no message to anyone.
Finish with one line per agent: what it wrote.
```

## CoS – Morning
```
{PREAMBLE}
Run type: MORNING. Load chief-of-staff and follow its MORNING section. Send no message.
Finish with one line: today's three priorities, actions executed, and whether the fallback planning ran.
```

## CoS – Evening
```
{PREAMBLE}
Run type: EVENING. Load chief-of-staff and follow its EVENING section (plan tomorrow, write the mode,
schedule tomorrow's window and key-session post check-ins using the WINDOW and POST templates from
schedules/templates.md). Send no message.
Finish with one line: tomorrow's mode, the window times, and what you scheduled.
```

## WINDOW (one-shot; name `CoS – <Wake|Home|Wind-down> – {DAY}`)
```
{PREAMBLE}
Run type: WINDOW, window {WINDOW}, date {DATE}. Load chief-of-staff and follow its WINDOW section.
The principal gets a push notification and may reply in this chat: handle replies as the skill's
"When he replies" section says.
```

## POST (one-shot; name `Coach – Post: <session> – {DAY}`)
```
{PREAMBLE}
Run type: POST for <session title>, which finished around <end> on {DATE}. Load running-coach and follow
its POST section (which loads nsm-coaching). Record this ping in pings/{DATE} before you send.
Then put this check-in on the Dashboard: ArtifactData set, collection "checkins",
doc_id "{DATE}-post-<slug>", data {"date","kind":"post","label":"Post: <session>","t":<epoch ms>,"url":"<this session's link>"}.
```

## Staff – weekly reports
```
{PREAMBLE}
Run type: WEEKLY. Load staff-protocol. Then, one after another, load and run the WEEKLY section of:
running-coach, lifestyle-coach, financial-advisor, business-coach, personal-development-coach.
Each writes reports/<agent>-<ISO week>. Send no message.
```

## CoS – Weekly
```
{PREAMBLE}
Run type: WEEKLY, and this is also Sunday's wind-down window. Load chief-of-staff and follow its WEEKLY
section, then send the review as the WINDOW section says. The principal replies in this chat.
```

## CoS – Monthly
```
{PREAMBLE}
Run type: MONTHLY. Load chief-of-staff and follow its MONTHLY section. The principal replies in this chat.
```
