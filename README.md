# Chief of Staff

A proactive, multi-agent system that helps run one person's life. A **Chief of Staff** agent manages five
specialist agents ("direct reports"), merges what they find, and is the only agent that messages the
principal, at fixed times of day.

| Agent | Area |
|---|---|
| `chief-of-staff` | Ranks and combines what the others find, settles conflicts, holds the approval queue, chases follow-ups, directs R&D |
| `running-coach` | Training, recovery, races (wraps the existing NSM coaching skill) |
| `lifestyle-coach` | Routines, habits, sleep, fuel, home, event/trip mode |
| `financial-advisor` | Weekly numbers, portfolio, runway, deadlines (education, not regulated advice) |
| `business-coach` | Building the running-coaching business |
| `personal-development-coach` | Growth goals chosen in an intake interview, reflection, start/stop |

The Dashboard (a private claude.ai artifact) is where everything is displayed. Its database is also how the
agents pass information to each other.

## Layout

```
.claude/skills/<agent>/SKILL.md   one skill per agent (logic only, no personal data)
.claude/skills/staff-protocol/    the shared reporting protocol every agent follows
contracts/data-model.md           Dashboard collections and document shapes
contracts/policy.md               autonomy, approvals, ping windows and budget
schedules/                        scheduled task plan and prompt templates
docs/architecture.md              design and build plan
```

## Privacy

This repository is public. It holds **no personal data**: no names, email addresses, account numbers,
figures or private links. Everything specific to the principal lives in the Dashboard's private database
(`agents/*`, `goals/*`, `house_rules/*`). Private links are passed in by the scheduled task prompts,
which are stored privately on the account.
