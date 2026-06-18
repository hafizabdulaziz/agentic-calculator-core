# Quickstart: Calculator Library

## Installation
Currently in development. Use local import.

## Basic Usage

```python
from calculator_project.calculator import Calculator

calc = Calculator()

# Addition
result = calc.add(10, 5)
print(f"10 + 5 = {result}")

# Division
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```
