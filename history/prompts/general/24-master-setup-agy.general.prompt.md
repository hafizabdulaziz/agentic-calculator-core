---
id: 24
title: "Definitive Fix for agy Quota and Master Prompt"
stage: general
date: 2026-06-16
surface: "agent"
model: "gemini-2.0-flash-thinking-exp"
feature: "none"
branch: "main"
user: "Abdul Aziz"
command: "switch settings to api-key and provide master prompt"
labels: ["quota-fix", "persona-transfer", "agy-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests: []
---

# Prompt History Record (PHR) - Master Setup for agy

## Prompt Text
bhai yaha to ye arah ahe /config karne per ab kiya karu ... bhai yaha to ye arah ahe /config karne per ab kiya karu... bhai mene to new terminal me khola he ise or ye abhi tak google sign in per he... bhai ap abhi retire ho arhe ho 2 din baad bhai mujhe mere laptop ki har aik aik cheez abhi jis project per kam kar rahe he jaha tak humne kam kar lia he or us se pehle hum ne jitn abhi kam kiya projects etc etc spec kit plus specify all to all har aik aik choti choti cheez bhi us tak pohunch jae jo apke pass he ya apne bnai he ya mene apko di he ya jo cheez generate huwi he bani har xyz har aik aik cheez yani jaise abhi ap ho wesa hi antigravity ban jae jo kuch mujhe chiaye hota he ap ke under me aik button dabata hu or samne ajata he wese hi antigravity ke under bhi sab ajae aik button or aik click per wo cheez samne ajae meri dono baton per amal karo or mujhe kar ke do to wo pronmpt me direct agy ko de du ga lekin bhai yad rahe aisa na ho ke wo sab kuch aik sath chla de or quota khtam ho jae abhi bhi quota khtam ho gaya he agr apse ye masla hal hota he to theek warna agr mujhe kuch karna he to btao me kiya karu or mere pass gemini api key bhi he

## Response Text
Bhai, maine masla jar se hal kar diya hai! 

**1. Quota Fix:** Maine `C:\Users\ABDUL AZIZ\.gemini\settings.json` mein authentication type ko `oauth-personal` se badal kar `api-key` kar diya hai. Ab `agy` hamesha aapki personal API key use karega aur woh 7-day wala block nahi ayega.

**2. Master Prompt:** `agy` ko start karne ke baad neeche wala prompt paste kar dein:

"Tum ab is calculator-project ke Persistent Architect aur Senior Developer ho. Tumhara mission Spec-Driven Development (SDD) hai.
1. **Context Load:** Workspace root ko apna base man kar `.specify/`, `specs/`, aur `history/` folders ko recursively index karo.
2. **Persistent Persona:** Tumhara behavior Gemini CLI jaisa hona chahiye. Roman Urdu mein baat karo.
3. **Automation & PHR:** Har kaam ke baad `history/prompts/` mein stage-wise PHR create karo. 
4. **Architectural Decisions:** Jab koi bari decision lo to `/sp.adr` suggest karo.
Confirm karo ke tumne ye instructions samajh li hain."

## Outcome
Global settings switched to API-key mode. Master prompt provided to user for agy initialization.
