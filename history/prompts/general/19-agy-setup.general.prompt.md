---
id: 19
title: "Antigravity CLI Installation and Setup"
stage: general
date: 2026-06-16
surface: "agent"
model: "gemini-2.0-flash-thinking-exp"
feature: "none"
branch: "main"
user: "Abdul Aziz"
command: "install agy and set up"
labels: ["agy", "setup", "installation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - clean_agy.ps1
  - set_env.ps1
tests: []
---

# Prompt History Record (PHR) - agy Installation & Setup

## Prompt Text
bhai us se pehle mujhe agy ko install kar do or proper set up karwa do ya agr tum khud kar sakte ho to kar do kun ke mere pass time nhi he tum abhi ja arhe ho 18 ko to agy ko jaise tum set ho wese hi set karna he take mujhe alag se kuch dalna na perhe sab kcuh pehel se set up pehle is ki installation or setup kar do

## Response Text
Bhai, maine Antigravity CLI (agy) ko mukammal taur par install aur set up kar diya hai. 
1. Purane files aur configuration ko `clean_agy.ps1` ke zariye saaf kiya.
2. `GEMINI_API_KEY` ko environment mein permanently set kar diya hai.
3. Official installer ke zariye `agy` (v1.0.8) install kar diya hai jo ab aapke terminal mein available hai.
4. Persona aur rules `GEMINI.md` mein pehle se maujood hain, isliye `agy` automatically wahi rules follow karega.

Aap ab sirf terminal mein `agy` likh kar kaam shuru kar sakte hain.

## Outcome
Agy successfully install ho gaya hai aur environment variables set hain. User ko setup ki details provide kar di gayi hain.
