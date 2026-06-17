---
id: 31
title: List available commands starting with /sp
stage: general
date: 2026-06-17
surface: agent
model: Gemini 3.5 Flash (Medium)
feature: none
branch: 001-basic-calculator-ops
user: Abdul Aziz
command: none
labels: ["help", "commands"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
tests:
---

## Prompt

List available commands starting with /sp

## Response snapshot

Haan ji Abdul Aziz, ye hain available commands jo `/sp` se shuru hoti hain:

1. **/sp.specify**: Kisi natural language feature description se feature specification (`spec.md`) create ya update karne ke liye.
2. **/sp.clarify**: Feature spec mein jo cheezain clear nahi hain unko identify karne ke liye aur maximum 5 targeted questions pooch kar unke answers spec mein add karne ke liye.
3. **/sp.plan**: Plan template ko use karte hue architectural aur design planning workflow execute karne ke liye.
4. **/sp.tasks**: Feature ke liye design artifacts ki base par actionable aur dependency-ordered `tasks.md` generate karne ke liye.
5. **/sp.analyze**: `spec.md`, `plan.md`, aur `tasks.md` ke darmiyan cross-artifact consistency aur quality check karne ke liye.
6. **/sp.implement**: `tasks.md` mein defined saare tasks ko process aur execute karne ke liye.
7. **/sp.adr**: Planning artifacts mein se architecturally significant decisions ko review kar ke Architecture Decision Records (ADRs) create karne ke liye.
8. **/sp.constitution**: Project constitution (`.specify/memory/constitution.md`) ko create ya update karne ke liye.
9. **/sp.git.commit_pr**: Ek autonomous Git workflow chalane ke liye jo code commit karega aur PR create karega.
10. **/sp.phr**: Har AI exchange ko Prompt History Record (PHR) ke taur par record karne ke liye taake learning aur traceability rahe.
11. **/sp.checklist**: User requirements ke mutabiq current feature ke liye custom checklist generate karne ke liye.
12. **/sp.reverse-engineer**: Codebase ko reverse engineer kar ke SDD-RI artifacts (spec, plan, tasks, intelligence) mein convert karne ke liye.
13. **/sp.taskstoissues**: Maujooda tasks ko actionable aur dependency-ordered GitHub issues mein convert karne ke liye.

## Outcome

- ✅ Impact: User was informed about all available /sp commands.
- 🧪 Tests: none
- 📁 Files: none
- 🔁 Next prompts: none
- 🧠 Reflection: Providing command listings in Roman Urdu helps keep consistency with user preferences and improves accessibility.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
