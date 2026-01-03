#!/usr/bin/env python3
"""
Num - A primitive data type that behaves like an integer with constrained range (1-10)

This module provides a Num class that validates input and ensures values stay within
the range of 1 to 10, with support for arithmetic operations, comparisons, and
proper error handling.

Author: Jordan Leturgez
Version: 1.0.0
"""

import numbers
import math
from typing import Union, Any


class Num:
    """
    A primitive data type that behaves like an integer with a lowest valid value of 1 
    and a highest valid value of 10.
    
    Attributes:
        value (int): The validated integer value between 1 and 10
        
    Raises:
        TypeError: If value is not a number or out of range
    """
    
    MIN_VALUE = 1
    MAX_VALUE = 10
    
    def __init__(self, value: Union[int, float, str]):
        """
        Initialize a Num instance with validation.
        
        Args:
            value: The value to convert to Num (int, float, or string representation)
            
        Raises:
            TypeError: If value is not a valid number or out of range
        """
        self.value = self._validate_and_convert(value)
    
    def _validate_and_convert(self, value: Any) -> int:
        """
        Validate and convert the input value to an integer.
        
        Args:
            value: The input value to validate
            
        Returns:
            int: The validated integer value
            
        Raises:
            TypeError: If value is not a valid number or out of range
        """
        # Handle None
        if value is None:
            raise TypeError("Not a Number")
        
        # Handle string inputs
        if isinstance(value, str):
            try:
                # Try to convert string to float first
                float_value = float(value.strip())
                return self._validate_numeric_value(float_value)
            except (ValueError, AttributeError):
                raise TypeError("Not a Number")
        
        # Handle numeric inputs
        if isinstance(value, numbers.Real):
            return self._validate_numeric_value(value)
        
        # Handle complex numbers and other types
        if isinstance(value, numbers.Complex):
            if value.imag != 0:
                raise TypeError("Not a Number")
            return self._validate_numeric_value(value.real)
        
        # Invalid type
        raise TypeError("Not a Number")
    
    def _validate_numeric_value(self, value: float) -> int:
        """
        Validate that a numeric value is within the valid range.
        
        Args:
            value: The numeric value to validate
            
        Returns:
            int: The integer value
            
        Raises:
            TypeError: If value is NaN, infinite, not a whole number, or out of range
        """
        # Check for NaN or infinity
        if math.isnan(value) or math.isinf(value):
            raise TypeError("Not a Number")
        
        # Check if it's a whole number
        if not self._is_whole_number(value):
            raise TypeError("Not a Number")
        
        # Convert to int and check range
        int_value = int(value)
        
        if int_value < self.MIN_VALUE or int_value > self.MAX_VALUE:
            raise TypeError("Out of range")
        
        return int_value
    
    def _is_whole_number(self, value: float) -> bool:
        """
        Check if a float value is a whole number.
        
        Args:
            value: The float value to check
            
        Returns:
            bool: True if the value is a whole number
        """
        return abs(value - round(value)) < 1e-10
    
    def __add__(self, other: 'Num') -> int:
        """
        Add two Num instances.
        
        Args:
            other: The Num to add
            
        Returns:
            int: The sum of the two values
        """
        if not isinstance(other, Num):
            raise TypeError("Can only add Num instances")
        return self.value + other.value
    
    def __sub__(self, other: 'Num') -> int:
        """
        Subtract another Num from this Num.
        
        Args:
            other: The Num to subtract
            
        Returns:
            int: The difference of the two values
        """
        if not isinstance(other, Num):
            raise TypeError("Can only subtract Num instances")
        return self.value - other.value
    
    def __mul__(self, other: 'Num') -> int:
        """
        Multiply two Num instances.
        
        Args:
            other: The Num to multiply by
            
        Returns:
            int: The product of the two values
        """
        if not isinstance(other, Num):
            raise TypeError("Can only multiply Num instances")
        return self.value * other.value
    
    def __truediv__(self, other: 'Num') -> float:
        """
        Divide this Num by another Num.
        
        Args:
            other: The Num to divide by
            
        Returns:
            float: The quotient of the two values
            
        Raises:
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, Num):
            raise TypeError("Can only divide Num instances")
        if other.value == 0:
            raise ZeroDivisionError("division by zero")
        return self.value / other.value
    
    def __floordiv__(self, other: 'Num') -> int:
        """
        Floor divide this Num by another Num.
        
        Args:
            other: The Num to divide by
            
        Returns:
            int: The floor quotient of the two values
            
        Raises:
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, Num):
            raise TypeError("Can only divide Num instances")
        if other.value == 0:
            raise ZeroDivisionError("division by zero")
        return self.value // other.value
    
    def __mod__(self, other: 'Num') -> int:
        """
        Modulo operation with another Num.
        
        Args:
            other: The Num to modulo by
            
        Returns:
            int: The remainder of the division
            
        Raises:
            ZeroDivisionError: If dividing by zero
        """
        if not isinstance(other, Num):
            raise TypeError("Can only modulo Num instances")
        if other.value == 0:
            raise ZeroDivisionError("division by zero")
        return self.value % other.value
    
    def __pow__(self, other: 'Num') -> int:
        """
        Raise this Num to the power of another Num.
        
        Args:
            other: The exponent Num
            
        Returns:
            int: The result of the exponentiation
        """
        if not isinstance(other, Num):
            raise TypeError("Can only exponentiate Num instances")
        return self.value ** other.value
    
    def __lt__(self, other: 'Num') -> bool:
        """
        Check if this Num is less than another Num.
        
        Args:
            other: The Num to compare to
            
        Returns:
            bool: True if this Num is less than the other
        """
        if not isinstance(other, Num):
            raise TypeError("Can only compare Num instances")
        return self.value < other.value
    
    def __le__(self, other: 'Num') -> bool:
        """
        Check if this Num is less than or equal to another Num.
        
        Args:
            other: The Num to compare to
            
        Returns:
            bool: True if this Num is less than or equal to the other
        """
        if not isinstance(other, Num):
            raise TypeError("Can only compare Num instances")
        return self.value <= other.value
    
    def __gt__(self, other: 'Num') -> bool:
        """
        Check if this Num is greater than another Num.
        
        Args:
            other: The Num to compare to
            
        Returns:
            bool: True if this Num is greater than the other
        """
        if not isinstance(other, Num):
            raise TypeError("Can only compare Num instances")
        return self.value > other.value
    
    def __ge__(self, other: 'Num') -> bool:
        """
        Check if this Num is greater than or equal to another Num.
        
        Args:
            other: The Num to compare to
            
        Returns:
            bool: True if this Num is greater than or equal to the other
        """
        if not isinstance(other, Num):
            raise TypeError("Can only compare Num instances")
        return self.value >= other.value
    
    def __eq__(self, other: object) -> bool:
        """
        Check if this Num is equal to another Num.
        
        Args:
            other: The object to compare to
            
        Returns:
            bool: True if this Num is equal to the other
        """
        if not isinstance(other, Num):
            return False
        return self.value == other.value
    
    def __ne__(self, other: object) -> bool:
        """
        Check if this Num is not equal to another Num.
        
        Args:
            other: The object to compare to
            
        Returns:
            bool: True if this Num is not equal to the other
        """
        return not self.__eq__(other)
    
    def __str__(self) -> str:
        """Return string representation of the Num."""
        return str(self.value)
    
    def __repr__(self) -> str:
        """Return detailed string representation of the Num."""
        return f"Num({self.value})"
    
    def __int__(self) -> int:
        """Return the integer value of the Num."""
        return self.value
    
    def __float__(self) -> float:
        """Return the float value of the Num."""
        return float(self.value)
    
    def __bool__(self) -> bool:
        """Return boolean representation of the Num."""
        return self.value != 0
    
    def __abs__(self) -> 'Num':
        """Return absolute value as a new Num."""
        return Num(abs(self.value))
    
    def __neg__(self) -> 'Num':
        """Return negative value as a new Num."""
        return Num(-self.value)
    
    def __pos__(self) -> 'Num':
        """Return positive value as a new Num."""
        return Num(self.value)
    
    def copy(self) -> 'Num':
        """Return a copy of this Num."""
        return Num(self.value)
    
    @classmethod
    def from_string(cls, value: str) -> 'Num':
        """
        Create a Num from a string representation.
        
        Args:
            value: The string to convert
            
        Returns:
            Num: A new Num instance
            
        Raises:
            TypeError: If the string is not a valid number
        """
        return cls(value)
    
    @classmethod
    def from_int(cls, value: int) -> 'Num':
        """
        Create a Num from an integer.
        
        Args:
            value: The integer to convert
            
        Returns:
            Num: A new Num instance
            
        Raises:
            TypeError: If the integer is out of range
        """
        return cls(value)
    
    @classmethod
    def from_float(cls, value: float) -> 'Num':
        """
        Create a Num from a float.
        
        Args:
            value: The float to convert
            
        Returns:
            Num: A new Num instance
            
        Raises:
            TypeError: If the float is not a whole number or out of range
        """
        return cls(value)
    
    @staticmethod
    def is_valid_value(value: Union[int, float, str]) -> bool:
        """
        Check if a value would be valid for creating a Num.
        
        Args:
            value: The value to check
            
        Returns:
            bool: True if the value is valid
        """
        try:
            Num(value)
            return True
        except TypeError:
            return False
    
    @staticmethod
    def get_min_value() -> int:
        """Return the minimum valid value."""
        return Num.MIN_VALUE
    
    @staticmethod
    def get_max_value() -> int:
        """Return the maximum valid value."""
        return Num.MAX_VALUE


# Test suite
def test_num_class():
    """Comprehensive test suite for the Num class."""
    print("=== Num Primitive Data Type Test Suite ===\n")
    
    # Test counters
    passed = 0
    failed = 0
    
    # Test 1: Basic instantiation
    print("Test 1: Basic Instantiation")
    try:
        n1 = Num(5)
        n2 = Num(3)
        print(f"✓ Created Num(5) and Num(3)")
        print(f"  Num(5).toString() = \"{str(n1)}\"")
        print(f"  Num(3).toString() = \"{str(n2)}\"")
        print(f"  repr(Num(5)) = {repr(n1)}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 2: Arithmetic operations
    print("\nTest 2: Arithmetic Operations")
    try:
        n1 = Num(3)
        n2 = Num(4)
        print(f"✓ Addition: Num(3) + Num(4) = {n1 + n2}")
        print(f"✓ Subtraction: Num(3) - Num(4) = {n1 - n2}")
        print(f"✓ Multiplication: Num(3) * Num(4) = {n1 * n2}")
        print(f"✓ Division: Num(3) / Num(4) = {n1 / n2}")
        print(f"✓ Floor Division: Num(7) // Num(3) = {Num(7) // n2}")
        print(f"✓ Modulo: Num(7) % Num(3) = {Num(7) % n2}")
        print(f"✓ Power: Num(2) ** Num(3) = {Num(2) ** Num(3)}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 3: Comparison operations
    print("\nTest 3: Comparison Operations")
    try:
        n1 = Num(3)
        n2 = Num(4)
        print(f"✓ Num(3) < Num(4) = {n1 < n2}")
        print(f"✓ Num(3) > Num(4) = {n1 > n2}")
        print(f"✓ Num(3) == Num(4) = {n1 == n2}")
        print(f"✓ Num(3) != Num(4) = {n1 != n2}")
        print(f"✓ Num(3) <= Num(4) = {n1 <= n2}")
        print(f"✓ Num(3) >= Num(4) = {n1 >= n2}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 4: Error handling - Not a Number
    print("\nTest 4: Error Handling - Not a Number")
    try:
        n = Num("test")
        print("✗ Should have thrown exception")
        failed += 1
    except TypeError as e:
        print(f"✓ Correctly threw: {e}")
        passed += 1
    
    # Test 5: Error handling - Out of range (low)
    print("\nTest 5: Error Handling - Out of Range (Low)")
    try:
        n = Num(0)
        print("✗ Should have thrown exception")
        failed += 1
    except TypeError as e:
        print(f"✓ Correctly threw: {e}")
        passed += 1
    
    # Test 6: Error handling - Out of range (high)
    print("\nTest 6: Error Handling - Out of Range (High)")
    try:
        n = Num(11)
        print("✗ Should have thrown exception")
        failed += 1
    except TypeError as e:
        print(f"✓ Correctly threw: {e}")
        passed += 1
    
    # Test 7: String constructor
    print("\nTest 7: String Constructor")
    try:
        n1 = Num("5")
        n2 = Num("3.0")
        print(f"✓ Created Num from string '5': {n1}")
        print(f"✓ Created Num from string '3.0': {n2}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 8: Double constructor
    print("\nTest 8: Double Constructor")
    try:
        n1 = Num(5.0)
        n2 = Num(3.0)
        print(f"✓ Created Num from float 5.0: {n1}")
        print(f"✓ Created Num from float 3.0: {n2}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 9: Factory methods
    print("\nTest 9: Factory Methods")
    try:
        n1 = Num.from_string("7")
        n2 = Num.from_int(8)
        n3 = Num.from_float(9.0)
        print(f"✓ Num.from_string('7') = {n1}")
        print(f"✓ Num.from_int(8) = {n2}")
        print(f"✓ Num.from_float(9.0) = {n3}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 10: Utility methods
    print("\nTest 10: Utility Methods")
    try:
        print(f"✓ Min value: {Num.get_min_value()}")
        print(f"✓ Max value: {Num.get_max_value()}")
        print(f"✓ Is 5 valid? {Num.is_valid_value(5)}")
        print(f"✓ Is 0 valid? {Num.is_valid_value(0)}")
        print(f"✓ Is 11 valid? {Num.is_valid_value(11)}")
        
        n = Num(5)
        print(f"✓ int(Num(5)) = {int(n)}")
        print(f"✓ float(Num(5)) = {float(n)}")
        print(f"✓ bool(Num(5)) = {bool(n)}")
        print(f"✓ abs(Num(-5)) = {abs(Num(-5))}")
        print(f"✓ -Num(5) = {-Num(5)}")
        print(f"✓ +Num(5) = {+Num(5)}")
        print(f"✓ Num(5).copy() = {n.copy()}")
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Test 11: Edge cases
    print("\nTest 11: Edge Cases")
    try:
        # Test boundary values
        n1 = Num(1)  # Minimum
        n2 = Num(10)  # Maximum
        print(f"✓ Boundary values work: Num(1) = {n1}, Num(10) = {n2}")
        
        # Test string with whitespace
        n3 = Num("  5  ")
        print(f"✓ String with whitespace: Num('  5  ') = {n3}")
        
        # Test scientific notation
        n4 = Num("5e0")
        print(f"✓ Scientific notation: Num('5e0') = {n4}")
        
        passed += 1
    except Exception as e:
        print(f"✗ Failed: {e}")
        failed += 1
    
    # Summary
    print(f"\n=== Test Summary ===")
    print(f"✓ Passed: {passed}")
    print(f"✗ Failed: {failed}")
    print(f"Total: {passed + failed}")
    print(f"Success Rate: {(passed/(passed+failed)*100):.1f}%")
    
    return passed, failed


# Example usage and demonstrations
def demonstrate_num_usage():
    """Demonstrate practical usage of the Num class."""
    print("\n=== Num Usage Demonstrations ===\n")
    
    print("1. Creating Num instances:")
    print(f"   Num(5) = {Num(5)}")
    print(f"   Num('7') = {Num('7')}")
    print(f"   Num(3.0) = {Num(3.0)}")
    
    print("\n2. Arithmetic operations:")
    a, b = Num(3), Num(4)
    print(f"   Num(3) + Num(4) = {a + b}")
    print(f"   Num(3) - Num(4) = {a - b}")
    print(f"   Num(3) * Num(4) = {a * b}")
    print(f"   Num(3) / Num(4) = {a / b}")
    
    print("\n3. Comparison operations:")
    x, y = Num(3), Num(4)
    print(f"   Num(3) < Num(4) = {x < y}")
    print(f"   Num(3) > Num(4) = {x > y}")
    print(f"   Num(3) == Num(4) = {x == y}")
    
    print("\n4. Error handling examples:")
    examples = ["invalid", 0, 11, None, float('inf'), 3.14]
    for example in examples:
        try:
            Num(example)
            print(f"   Num({example}) = Success")
        except TypeError as e:
            print(f"   Num({example}) = Error: {e}")


if __name__ == "__main__":
    # Run the test suite
    test_num_class()
    
    # Run the demonstration
    demonstrate_num_usage()
