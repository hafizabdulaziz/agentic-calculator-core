# 🚀 Agentic Calculator Core

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![TDD](https://img.shields.io/badge/Built%20With-TDD%20%2F%20Pytest-orange?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)](https://github.com/hafizabdulaziz/agentic-calculator-core)

**Agentic Calculator Core** is a high-performance, type-safe mathematical engine specifically engineered for **Autonomous AI Agents** and **Multi-Agent Systems (MAS)**. 

Unlike standard calculators, this engine is designed as a **Deterministic Tool** for the **Model Context Protocol (MCP)**, ensuring that LLMs can perform complex arithmetic without the risk of probabilistic hallucinations.

---

## 🎯 The "AI-Native" Problem
LLMs are notoriously unreliable at mathematics because they predict the *next token* rather than executing *logic*. In a production autonomous system, a single math error can lead to catastrophic failure in downstream tasks.

### The Solution: Deterministic Tooling
`agentic-calculator-core` shifts the burden of computation from the **LLM's reasoning layer** to a **verified execution layer**:
- **Zero-Hallucination Guarantee:** Every operation is executed in a type-safe Python environment.
- **Agent-Optimized Interfaces:** Tool definitions are structured for maximum LLM discoverability and precision.
- **Strict Error Boundaries:** Instead of "guessing" a result, the engine returns explicit, machine-readable error states (e.g., `ZeroDivisionError`, `OverflowError`) which the agent can then reason about.

---

## 🏗 Technical Architecture

### Design Principles
1. **Deterministic Execution:** No stochastic elements in the computation path.
2. **Type Safety:** Rigorous use of Python 3.13+ type hinting for predictable inputs/outputs.
3. **TDD Validated:** 100% coverage of core mathematical primitives via Pytest.
4. **MCP Ready:** Built-in support for the Model Context Protocol to enable instant integration with Claude Desktop and other MCP-compatible hosts.

### Component Map
```text
agentic-calculator-core/
├── src/
│   └── calculator_project/
│       ├── engine.py       # Deterministic math logic & error handling
│       └── schema.py       # Type definitions for MCP tool-use
├── tests/
│   └── unit/               # TDD suite ensuring mathematical correctness
├── main.py                 # MCP Server entry point & CLI
└── pyproject.toml          # Modern UV-based dependency management
```

---

## 🛠 Tech Stack
- **Runtime:** Python 3.13.14+
- **Management:** [UV](https://github.com/astral-sh/uv) (High-performance package management)
- **Validation:** Pytest (Test-Driven Development)
- **Protocol:** Model Context Protocol (MCP)

---

## 🚀 Deployment & Integration

### 1. Local Setup
```bash
git clone https://github.com/hafizabdulaziz/agentic-calculator-core.git
cd agentic-calculator-core
uv sync
```

### 2. Integration with MCP Hosts (e.g., Claude Desktop)
Add the following to your `claude_desktop_config.json`:

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

## 🗺 Roadmap
- [ ] **Advanced Calculus Support:** Integrating `sympy` for symbolic mathematics.
- [ ] **Unit Conversion Layer:** Adding deterministic physical unit conversions.
- [ ] **Financial Primitives:** Specialized tools for precision currency and interest calculations.

---

## 🌟 Author
**Hafiz Abdul Aziz** | AI-Native Engineer
[GitHub](https://github.com/hafizabdulaziz) | [LinkedIn](https://linkedin.com/in/hafizabdulaziz)
