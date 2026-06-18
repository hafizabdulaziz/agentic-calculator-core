# Agentic Calculator Core 🤖🧮

[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TDD Built](https://img.shields.io/badge/Built%20With-TDD%20%2F%20Pytest-orange?style=flat-square&logo=pytest&logoColor=white)](https://docs.pytest.org/)

A robust, type-safe, and highly-optimized mathematical execution engine built specifically to act as an external tool for autonomous AI Agents, LLMs, and Model Context Protocol (MCP) frameworks.

---

## 🌟 Why Agentic?
Large Language Models (LLMs) inherently struggle with precise multi-step arithmetic and mathematical reasoning due to their token-prediction nature. `agentic-calculator-core` provides a standardized programmatic interface, clear error boundaries, and deterministic execution profiles that autonomous agents can invoke reliably without breaking their logical context or causing runtime crashes.

---

## 🛠 Technical Highlights
* **Python 3.13+** native optimization and typed structures.
* Built strictly using **Test-Driven Development (TDD)** with a comprehensive `pytest` suite.
* Clean error boundary handling (division by zero, negative roots, float overflow/underflow).
* Fast environment management and locking via **UV**.
* Zero external runtime dependencies for maximum security and minimal footprint.

---

## 📂 Project Architecture
```
agentic-calculator-core/
├── src/
│   └── calculator_project/
│       ├── __init__.py
│       └── calculator.py       # Core execution logic
├── tests/
│   └── unit/
│       └── test_calculator.py  # Comprehensive TDD verification suite
├── pyproject.toml              # Dependencies & build configuration
└── main.py                     # Entry point
```

---

## 🚀 Setup & Usage

Ensure you have [uv](https://github.com/astral-sh/uv) installed for blazing-fast package management:

### 1. Install Dependencies
```bash
uv sync
```

### 2. Run the Main Interactive CLI
```bash
uv run python main.py
```

### 3. Run the Rigorous Test Suite
```bash
uv run pytest --cov=src --cov-report=term-missing
```

---

## 🤝 Model Context Protocol (MCP) Integration
To expose this calculator directly to Claude Desktop or any MCP-compatible agent host, add the following to your `mcp_config.json`:

```json
{
  "mcpServers": {
    "agentic-calculator": {
      "command": "uv",
      "args": ["run", "python", "C:/path/to/agentic-calculator-core/main.py"]
    }
  }
}
```

---
*Optimized & Maintained with pride by **[Hafiz Abdul Aziz](https://github.com/hafizabdulaziz)**.*
