---
ID: 15
TITLE: clean-reinstall-of-agy
STAGE: general
DATE_ISO: 2026-06-16
SURFACE: agent
MODEL: gemini-cli
FEATURE: none
BRANCH: main
USER: ABDUL AZIZ
COMMAND: .\clean_agy.ps1
LABELS: ["cleanup", "reinstall", "agy"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - clean_agy.ps1
TESTS_YAML:
  - none
PROMPT_TEXT: "User requested a complete removal and clean re-installation of the Antigravity CLI to resolve persistent quota issues. Created a PowerShell script (clean_agy.ps1) to uninstall agy, remove configuration files, and clear environment variables."
RESPONSE_TEXT: "Provided a clean-up script (clean_agy.ps1) and instructions for fresh installation followed by immediate API key configuration."
OUTCOME: "Clean re-installation initiated"
EVALUATION: "Success"
---
# Clean Re-installation of Antigravity CLI

User requested a complete removal and clean re-installation of the Antigravity CLI to resolve persistent quota issues. Created a PowerShell script (clean_agy.ps1) to uninstall agy, remove configuration files, and clear environment variables.
