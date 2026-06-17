class Calculator:
    """Main Calculator class providing basic arithmetic operations."""

    def add(self, a: int | float, b: int | float) -> float:
        """
        Add two numbers and return the sum as a float.

        Args:
            a (int | float): The first number.
            b (int | float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return float(a + b)

    def subtract(self, a: int | float, b: int | float) -> float:
        """
        Subtract one number from another and return the result as a float.

        Args:
            a (int | float): The number to subtract from (minuend).
            b (int | float): The number to subtract (subtrahend).

        Returns:
            float: The difference between a and b.
        """
        return float(a - b)

    def multiply(self, a: int | float, b: int | float) -> float:
        """
        Multiply two numbers and return the product as a float.

        Args:
            a (int | float): The first number.
            b (int | float): The second number.

        Returns:
            float: The product of a and b.
        """
        return float(a * b)

    def divide(self, a: int | float, b: int | float) -> float:
        """
        Divide one number by another and return the result as a float.

        Args:
            a (int | float): The dividend.
            b (int | float): The divisor.

        Returns:
            float: The quotient of a divided by b.

        Raises:
            ValueError: If the divisor (b) is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return float(a / b)
