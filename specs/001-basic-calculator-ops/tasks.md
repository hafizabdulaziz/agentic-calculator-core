# Tasks: Basic Calculator Operations

**Input**: Design documents from `/specs/001-basic-calculator-ops/`
**Prerequisites**: plan.md, spec.md, research.md, contracts/calculator_api.py

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize project using `uv init --lib`
- [x] T002 [P] Configure `pyproject.toml` with `pytest` and `mypy` using `uv add --dev`
- [x] T003 [P] Verify project structure and `.python-version`
- [ ] **Review**: Phase 1 approval from user.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core interface and skeleton that MUST be complete before ANY user story can be implemented

- [x] T004 Create skeleton `Calculator` class in `src/calculator_project/calculator.py` implementing `CalculatorContract`

**Checkpoint**: Foundation ready - user story implementation can now begin.
- [ ] **Review**: Phase 2 approval from user.

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Implement addition, subtraction, multiplication, and division as a library core.

**Independent Test**: `tests/unit/test_calculator.py` covering all 4 operations with valid inputs.

### Implementation for User Story 1

- [x] T005 [P] [US1] Write RED tests for `add`, `subtract`, `multiply`, `divide` in `tests/unit/test_calculator.py`
- [x] T010 [US1] Implement GREEN `add` in `src/calculator_project/calculator.py`
- [x] T011 [US1] Implement GREEN `subtract` in `src/calculator_project/calculator.py`
- [x] T012 [US1] Implement GREEN `multiply` in `src/calculator_project/calculator.py`
- [x] T013 [US1] Implement GREEN `divide` in `src/calculator_project/calculator.py`

**Checkpoint**: Basic arithmetic is functional and tested independently.
- [ ] **Review**: Phase 3 approval from user.

---

## Phase 4: User Story 2 - Error Handling (Priority: P2)

**Goal**: Ensure division by zero raises a clear `ValueError` with "Cannot divide by zero" message.

**Independent Test**: Test case `test_divide_by_zero` in `tests/unit/test_calculator.py`.

### Implementation for User Story 2

- [x] T014 [US2] Write RED test for division by zero in `tests/unit/test_calculator.py`
- [x] T015 [US2] Implement GREEN zero-division check in `src/calculator_project/calculator.py`

**Checkpoint**: Error handling for division by zero is verified.
- [ ] **Review**: Phase 4 approval from user.

---

## Phase 5: User Story 3 - Type Safety & Validation (Priority: P3)

**Goal**: Enforce strict type hints and validate code with static analysis.

**Independent Test**: `mypy --strict` execution result.

### Implementation for User Story 3

- [x] T016 [US3] Apply strict type hints to all methods in `src/calculator_project/calculator.py`
- [x] T017 [US3] Run `mypy` validation for `src/calculator_project/calculator.py`

**Checkpoint**: Type safety verified.
- [ ] **Review**: Phase 5 approval from user.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation, cleanup, and verification.

- [x] T018 Add professional docstrings (PEP 257) to `src/calculator_project/calculator.py`
- [x] T019 [P] Final validation against `quickstart.md` using `quickstart_check.py`
- [x] T020 [P] Create implementation PHR record in `history/prompts/001-basic-calculator-ops/`

**Checkpoint**: Feature complete and verified.
- [ ] **Review**: Final Phase 6 approval from user.

---

## Dependencies & Execution Order

### Phase Dependencies
- **Phase 1 (Setup)**: None
- **Phase 2 (Foundational)**: Depends on Phase 1
- **User Stories (Phase 3-5)**: Depend on Phase 2 completion
- **Phase 6 (Polish)**: Depends on all User Stories

### Parallel Execution Examples
- **Setup**: T002 and T003 can run in parallel.
- **US1**: T005 (Tests) can be written in parallel with entity/model creation (if any).
- **Polish**: T019 and T020 can run in parallel.

## Implementation Strategy
- **MVP First**: User Story 1 (Basic Arithmetic) is the primary deliverable.
- **Incremental Delivery**: Followed by Error Handling (US2) and Type Safety (US3).
- **TDD Flow**: Each story follows the RED -> GREEN -> REFACTOR cycle.
