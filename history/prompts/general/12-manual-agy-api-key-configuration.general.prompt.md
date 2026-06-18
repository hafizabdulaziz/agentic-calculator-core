---
ID: 12
TITLE: manual-agy-api-key-configuration
STAGE: general
DATE_ISO: 2026-06-16
SURFACE: agent
MODEL: gemini-cli
FEATURE: none
BRANCH: main
USER: ABDUL AZIZ
COMMAND: agy config set gemini_api_key
LABELS: ["troubleshooting", "agy", "setup"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - none
TESTS_YAML:
  - none
PROMPT_TEXT: "User reported that the automated setup script failed to bypass the Antigravity CLI quota. Provided manual commands to set the API key in agy configuration and environment variables."
RESPONSE_TEXT: "Provided manual commands to set API key in agy configuration and via environment variables. Suggested using an API key flag as a fallback for bypassing the starter quota."
OUTCOME: "Manual configuration instructions provided"
EVALUATION: "Success"
---
# Manual Antigravity API Key Configuration

User reported that the automated setup script failed to bypass the Antigravity CLI quota. Provided manual commands to set the API key in agy configuration and environment variables.
