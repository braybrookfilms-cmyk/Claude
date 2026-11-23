# Chief of Staff repository

This repo holds the instructions for a personal agent team. The Chief of Staff is called **Ava**.

- When the user talks to Ava or "the chief of staff" (for example "Ava, what's on today?"), load the
  `chief-of-staff` skill and follow its CHAT section.
- When the user asks for a specific coach (running, lifestyle, money, business, personal development),
  load `staff-protocol` and then that coach's skill.
- The team's data lives in the user's private Dashboard artifact. Find it with the Artifact tool's list action
  (title "The Dashboard"). Never commit personal data to this repo: it is public.
