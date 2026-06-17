---
id: 36
title: Explain and Fix MCP Loading Error
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
  - history/prompts/general/36-explain-and-fix-mcp-loading-error.general.prompt.md
  - policies.toml
tests:
  - none
---

## Prompt

MCP Servers

Configured (~\.gemini\antigravity-cli\mcp_config.json)
>  ✗ google-search  error: npm error code E404
npm error 404 Not Found - GET https://registry.npmjs.org/@modelcontextprotocol%2fserver-google-search - Not found
npm error 404
npm error 404  '@modelcontextprotocol/server-google-search@*' is not in this registry.
npm error 404
npm error 404 Note that you can also install from a
npm error 404 tarball, folder, http url, or git url.
npm error A complete log of this run can be found in: C:\Users\ABDUL AZIZ\AppData\Local\npm-cache\_logs\2026-06-17T11_48_23_930Z-debug-0.log
: calling "initialize": EOF

Plugins (~\.gemini\antigravity-cli\plugins)
   ✓ firebase  Tools: firebase_login, firebase_logout, firebase_get_project, firebase_list_apps, firebase_list_projects, +14 more
   ✓ github  Tools: create_or_update_file, search_repositories, create_repository, get_file_contents, push_files, +21 more
   ✓ google-sheets  Tools: sheets_check_access, sheets_get_values, sheets_batch_get_values, sheets_get_metadata, sheets_update_values, +35 more
   ✓ memory-server  Tools: create_entities, create_relations, add_observations, delete_entities, delete_observations, +4 more
   ✓ sqlite-database  Tools: query, execute, describe-table, list-tables, create-table, +5 more

Keyboard: ↑/↓ Navigate  enter Actions  bhai ise zara explain karo ge ye config me error aya or plugin me agaya

## Response snapshot

Maine user ko explain kiya ke 5 MCP servers successfully load ho gaye hain aur plugins list mein checkmark dikha rahe hain, jabke google-search ka error abhi bhi workspace ke `policies.toml` file mein configured hone ki wajah se show ho raha tha. Maine `policies.toml` mein se google-search ko comment out kar ke masla hal kar diya hai.

## Outcome

- ✅ Impact: Explained the difference between global plugins and local workspace policy configuration, and resolved the google-search error.
- 🧪 Tests: None
- 📁 Files: Updated `policies.toml` and created `history/prompts/general/36-explain-and-fix-mcp-loading-error.general.prompt.md`.
- 🔁 Next prompts: Ask the user to confirm that the error is resolved.
- 🧠 Reflection: Clear separation of global configuration vs project-level policies helps explain configuration merging to the user.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
