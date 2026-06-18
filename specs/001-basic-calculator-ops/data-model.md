# Data Model: Basic Calculator Operations

## Entities

### Calculator
Represented as a class that encapsulates arithmetic logic.
- **Methods**: `add`, `subtract`, `multiply`, `divide`.

### OperationInput
Inputs are standard Python numeric types (`int` or `float`).

### OperationResult
The result of any operation is a `float`.

## Validation Rules
- All inputs MUST be `int | float`.
- Divisor in `divide` operation MUST NOT be `0`.
