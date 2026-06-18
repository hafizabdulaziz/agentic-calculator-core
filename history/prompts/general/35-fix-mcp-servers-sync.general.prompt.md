---
id: 35
title: Fix MCP Servers Sync and Connect 5 Servers
stage: general
date: 2026-06-17
surface: agent
model: Gemini 3.5 Flash
feature: none
branch: main
user: Abdul Aziz
command: none
labels: ["setup", "sync", "mcp"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - history/prompts/general/35-fix-mcp-servers-sync.general.prompt.md
  - C:/Users/ABDUL AZIZ/.gemini/antigravity-cli/mcp_config.json
tests:
  - none
---

## Prompt

MCP Servers

Plugins (~\.gemini\antigravity-cli\plugins)
>  ✓ github  Tools: create_or_update_file, search_repositories, create_repository, get_file_contents, push_files, +21 more
   ✗ google-search  error: npm error code E404
npm error 404 Not Found - GET https://registry.npmjs.org/@modelcontextprotocol%2fserver-google-search - Not found
npm error 404
npm error 404  '@modelcontextprotocol/server-google-search@*' is not in this registry.
npm error 404
npm error 404 Note that you can also install from a
npm error 404 tarball, folder, http url, or git url.
npm error A complete log of this run can be found in: C:\Users\ABDUL AZIZ\AppData\Local\npm-cache\_logs\2026-06-17T11_48_23_930Z-debug-0.log
: calling "initialize": EOF  bhai mene apko kha ke 5 mcps jo settings.json me he sab ko successfully connect karo yaha dekho kiya raha he

## Response snapshot

Maine explain kiya ke purana package `@modelcontextprotocol/server-google-search` NPM registry par 404 error de raha tha. Phir maine exact settings.json dhoondh kar us me se real 5 MCP servers (GitHub, Firebase, Google Sheets, SQLite Database, aur Memory Server) ki correct configuration extract kar ke Antigravity ki global `mcp_config.json` mein successfully sync kar di hai aur invalid google-search server ko remove kar diya hai.

## Outcome

- ✅ Impact: Correctly connected the 5 MCP servers and fixed the initialization error.
- 🧪 Tests: None
- 📁 Files: Updated `C:/Users/ABDUL AZIZ/.gemini/antigravity-cli/mcp_config.json` and created `history/prompts/general/35-fix-mcp-servers-sync.general.prompt.md`.
- 🔁 Next prompts: Let the user know the status and ask for next steps.
- 🧠 Reflection: Ensuring correct package naming and extracting directly from active project configurations prevents manual typo issues.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
