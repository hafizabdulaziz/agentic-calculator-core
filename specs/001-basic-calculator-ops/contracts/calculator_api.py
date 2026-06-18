from typing import Protocol

class CalculatorContract(Protocol):
    """Protocol defining the interface for the Calculator library."""

    def add(self, a: int | float, b: int | float) -> float:
        """Add two numbers."""
        ...

    def subtract(self, a: int | float, b: int | float) -> float:
        """Subtract b from a."""
        ...

    def multiply(self, a: int | float, b: int | float) -> float:
        """Multiply two numbers."""
        ...

    def divide(self, a: int | float, b: int | float) -> float:
        """Divide a by b. Raises ValueError if b is 0."""
        ...
