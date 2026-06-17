---
id: 28
title: "One-Click AGY Automation Setup"
stage: general
date_iso: 2026-06-17
surface: agent
model: gemini-2.0-flash-exp
feature: none
branch: main
user: Abdul Aziz
command: Create FULL_AGY_SETUP.ps1
labels: ["automation", "setup", "agy", "one-click"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - FULL_AGY_SETUP.ps1
  - agy_master_prompt.md
tests_yaml:
  - none
---

### PROMPT_TEXT
bhai to ye sara kam apkar do na mere behalf pe ap mujhe agy ko full setup kar ke do

### RESPONSE_TEXT
Maine aap ke liye 'FULL_AGY_SETUP.ps1' script bna di hai jo sab kuch automate kar degi. Ye script API key set karegi, project folders verify karegi, aur 'Master Prompt' ko khud hi clipboard par copy kar degi. Aap ko bas ye script run karni hai aur AGY mein prompt paste karna hai. Infrastructure ab mukammal taur par naye account ke liye tayyar hai.

### OUTCOME/EVALUATION
Automation script created. Setup for AGY is now a single execution process.
