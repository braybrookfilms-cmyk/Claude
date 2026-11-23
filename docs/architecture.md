# Architecture and build plan

## Principles
1. **One voice.** Specialists write to the Dashboard; only the Chief of Staff talks to the principal.
2. **Proactive by design.** Watches (trigger conditions), looking ahead 1, 7 and 30 days, leading measures,
   follow-up dates on everything, and proposals rather than reports. See `contracts/policy.md` §4.
3. **Limited, predictable pings.** Three windows a day (wake, home, wind-down), a hard cap of 3 pushes,
   and merging instead of adding.
4. **Permission matches impact.** R&D and internal work are free. Anything that affects his life or reaches
   other people goes through the approval queue. Money is never moved.
5. **Logic in the repo, personal data in the Dashboard.** Skills are generic and public; charters, goals,
   thresholds and links are private.
6. **Reuse what works.** The existing NSM coaching skill, house rules, mode, priorities, portfolio and the
   quest tracker are all kept and built on.

## Flow of a day
```
04:13  Staff sweep      run · life · money · biz · growth check their watches → signals / actions
04:45  CoS Morning      executes approved actions, expires stale items, sets top 3, writes briefs/<today>
wake   CoS window       brief + running coach's morning read + "Needs you" approvals       (ping 1)
       (key session)    running coach post check-in                                         (counts as a ping)
home   CoS window       what's left of today, what tomorrow needs prepared                  (ping 2)
19:13  CoS Evening      mode, transitions → signals, tomorrow's window times, one-shot tasks
wind-  CoS window       tomorrow's shape, the one thing to protect, wind-down nudge         (ping 3)
down
```
Sunday: Staff weekly reports at 19:37 → CoS Weekly review as the wind-down message.
1st of the month: CoS Monthly scorecard and start/stop.

## Phases
| Phase | Scope | Done when |
|---|---|---|
| **0 Groundwork** | Repo, contracts, policy, all six skills, schedule plan | ✅ this commit |
| **1 Core loop** | Seed `agents/*`; Morning, Evening and window tasks live; Running coach on signals; approvals working in chat | One week with ≤3 pings a day and at least one approval round-trip |
| **2 Dashboard HQ** | HQ tab: brief, approval queue (Approve, Decline, Snooze), agent status board, signal strips on each tab; Business and Growth tabs; tabs regrouped | He can approve from the Dashboard |
| **3 Life + Money** | Lifestyle and financial watches live; weekly numbers flow through the Sunday review | Two Sundays of numbers captured |
| **4 Biz + Growth** | Business coach reading the quest tracker; Growth intake interview; draft goals agreed | Growth goals `active` |
| **5 Tune** | After 2 weeks: which signals were acted on and which ignored; adjust thresholds and the ping budget; delete retired tasks | Noise is under 1 ignored signal a day |
