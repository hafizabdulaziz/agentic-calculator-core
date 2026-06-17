---
id: 33
title: List Available sp Commands
stage: general
date: 2026-06-17
surface: agent
model: Gemini 3.5 Flash
feature: none
branch: main
user: Abdul Aziz
command: none
labels: ["help", "commands"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - history/prompts/general/33-list-available-sp-commands.general.prompt.md
tests:
  - none
---

## Prompt

/sp.

## Response snapshot

Maine available `/sp.` commands ki list Roman Urdu mein share ki hai aur har command ke function ko briefly explain kiya hai taake user ko inke uses ka pata chale.

## Outcome

- ✅ Impact: Listed all available Spec Kit Plus commands for the user.
- 🧪 Tests: None
- 📁 Files: Created `history/prompts/general/33-list-available-sp-commands.general.prompt.md`.
- 🔁 Next prompts: Ask the user which command or task they want to execute next.
- 🧠 Reflection: Providing a clear list of commands maintains workflow consistency.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
