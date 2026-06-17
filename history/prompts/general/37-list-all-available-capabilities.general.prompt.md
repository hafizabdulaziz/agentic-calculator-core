---
id: 37
title: List All Available Capabilities A to Z
stage: general
date: 2026-06-17
surface: agent
model: Gemini 3.5 Flash
feature: none
branch: main
user: Abdul Aziz
command: none
labels: ["help", "status", "capabilities"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - history/prompts/general/37-list-all-available-capabilities.general.prompt.md
tests:
  - none
---

## Prompt

bhai abhi sirf ap mujhe text me ye bta do ke is waqt ap ke pass kiya kiya cheezain available he a to z jitni cheezain apke under mjood he mujhe btao

## Response snapshot

Maine user ko details ke sath Roman Urdu mein A to Z un tamam capabilities, files, tools, MCP servers, and configurations ki list di hai jo is waqt mere pass ready aur accessible hain.

## Outcome

- ✅ Impact: Provided a complete inventory of the agent's files, tools, settings, and MCP plugins.
- 🧪 Tests: None
- 📁 Files: Created `history/prompts/general/37-list-all-available-capabilities.general.prompt.md`.
- 🔁 Next prompts: Ask the user which feature or spec to start building next.
- 🧠 Reflection: Providing a clear list of what is loaded and active builds transparency and aligns next steps.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
