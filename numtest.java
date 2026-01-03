/**
 * Num - A primitive data type that behaves like an integer with constrained range (1-10)
 * 
 * @author Your Name
 * @version 1.0.0
 */
public class Num {
    private final int value;
    
    /**
     * Constructs a Num with the specified value
     * 
     * @param value the integer value between 1 and 10 (inclusive)
     * @throws IllegalArgumentException if value is not a number or out of range
     */
    public Num(int value) {
        validateValue(value);
        this.value = value;
    }
    
    /**
     * Constructs a Num from a double value
     * 
     * @param value the double value to be converted to integer
     * @throws IllegalArgumentException if value is not a whole number or out of range
     */
    public Num(double value) {
        if (Double.isNaN(value) || Double.isInfinite(value)) {
            throw new IllegalArgumentException("Not a Number");
        }
        
        int intValue = (int) value;
        
        // Check if the double is a whole number
        if (Math.abs(value - intValue) > 1e-10) {
            throw new IllegalArgumentException("Not a Number");
        }
        
        validateValue(intValue);
        this.value = intValue;
    }
    
    /**
     * Constructs a Num from a string representation
     * 
     * @param value the string representation of the number
     * @throws IllegalArgumentException if value is not a valid number or out of range
     */
    public Num(String value) {
        if (value == null || value.trim().isEmpty()) {
            throw new IllegalArgumentException("Not a Number");
        }
        
        try {
            double doubleValue = Double.parseDouble(value.trim());
            int intValue = (int) doubleValue;
            
            // Check if the string represents a whole number
            if (Math.abs(doubleValue - intValue) > 1e-10) {
                throw new IllegalArgumentException("Not a Number");
            }
            
            validateValue(intValue);
            this.value = intValue;
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Not a Number");
        }
    }
    
    /**
     * Validates that the value is within the valid range (1-10)
     * 
     * @param value the integer value to validate
     * @throws IllegalArgumentException if value is out of range
     */
    private void validateValue(int value) {
        if (value < 1 || value > 10) {
            throw new IllegalArgumentException("Out of range");
        }
    }
    
    /**
     * Returns the integer value
     * 
     * @return the integer value
     */
    public int getValue() {
        return value;
    }
    
    /**
     * Adds two Num instances
     * 
     * @param other the Num to add
     * @return the sum as a primitive int
     */
    public int add(Num other) {
        return this.value + other.value;
    }
    
    /**
     * Subtracts another Num from this Num
     * 
     * @param other the Num to subtract
     * @return the difference as a primitive int
     */
    public int subtract(Num other) {
        return this.value - other.value;
    }
    
    /**
     * Multiplies two Num instances
     * 
     * @param other the Num to multiply by
     * @return the product as a primitive int
     */
    public int multiply(Num other) {
        return this.value * other.value;
    }
    
    /**
     * Divides this Num by another Num
     * 
     * @param other the Num to divide by
     * @return the quotient as a primitive double
     * @throws ArithmeticException if dividing by zero
     */
    public double divide(Num other) {
        if (other.value == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return (double) this.value / other.value;
    }
    
    /**
     * Compares this Num with another Num
     * 
     * @param other the Num to compare to
     * @return true if this Num is less than the other Num
     */
    public boolean isLessThan(Num other) {
        return this.value < other.value;
    }
    
    /**
     * Compares this Num with another Num
     * 
     * @param other the Num to compare to
     * @return true if this Num is greater than the other Num
     */
    public boolean isGreaterThan(Num other) {
        return this.value > other.value;
    }
    
    /**
     * Compares this Num with another Num
     * 
     * @param other the Num to compare to
     * @return true if this Num is equal to the other Num
     */
    public boolean isEqualTo(Num other) {
        return this.value == other.value;
    }
    
    /**
     * Compares this Num with another Num
     * 
     * @param other the Num to compare to
     * @return true if this Num is less than or equal to the other Num
     */
    public boolean isLessThanOrEqualTo(Num other) {
        return this.value <= other.value;
    }
    
    /**
     * Compares this Num with another Num
     * 
     * @param other the Num to compare to
     * @return true if this Num is greater than or equal to the other Num
     */
    public boolean isGreaterThanOrEqualTo(Num other) {
        return this.value >= other.value;
    }
    
    /**
     * Compares this Num with another Num
     * 
     * @param other the Num to compare to
     * @return true if this Num is not equal to the other Num
     */
    public boolean isNotEqualTo(Num other) {
        return this.value != other.value;
    }
    
    @Override
    public String toString() {
        return String.valueOf(value);
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Num num = (Num) obj;
        return value == num.value;
    }
    
    @Override
    public int hashCode() {
        return Integer.hashCode(value);
    }
    
    @Override
    public int compareTo(Num other) {
        return Integer.compare(this.value, other.value);
    }
    
    // Implement Comparable interface
    public class Num implements Comparable<Num> {
        // ... existing code ...
        
        @Override
        public int compareTo(Num other) {
            return Integer.compare(this.value, other.value);
        }
    }
    
    /**
     * Static factory methods for creating Num instances
     */
    public static Num of(int value) {
        return new Num(value);
    }
    
    public static Num of(double value) {
        return new Num(value);
    }
    
    public static Num of(String value) {
        return new Num(value);
    }
    
    /**
     * Returns the maximum value (10)
     */
    public static int getMaxValue() {
        return 10;
    }
    
    /**
     * Returns the minimum value (1)
     */
    public static int getMinValue() {
        return 1;
    }
    
    /**
     * Checks if a value is within the valid range
     */
    public static boolean isValidValue(int value) {
        return value >= 1 && value <= 10;
    }
}

/**
 * Test class demonstrating Num functionality
 */
class NumTest {
    public static void main(String[] args) {
        System.out.println("=== Num Primitive Data Type Test Suite ===\n");
        
        // Test 1: Basic instantiation
        System.out.println("Test 1: Basic Instantiation");
        try {
            Num n1 = new Num(5);
            Num n2 = new Num(3);
            System.out.println("✓ Created Num(5) and Num(3)");
            System.out.println("  Num(5).toString() = \"" + n1.toString() + "\"");
            System.out.println("  Num(3).toString() = \"" + n2.toString() + "\"");
        } catch (Exception e) {
            System.out.println("✗ Failed: " + e.getMessage());
        }
        
        // Test 2: Arithmetic operations
        System.out.println("\nTest 2: Arithmetic Operations");
        try {
            Num n1 = new Num(3);
            Num n2 = new Num(4);
            System.out.println("✓ Addition: Num(3) + Num(4) = " + n1.add(n2));
            System.out.println("✓ Subtraction: Num(3) - Num(4) = " + n1.subtract(n2));
            System.out.println("✓ Multiplication: Num(3) * Num(4) = " + n1.multiply(n2));
            System.out.println("✓ Division: Num(3) / Num(4) = " + n1.divide(n2));
        } catch (Exception e) {
            System.out.println("✗ Failed: " + e.getMessage());
        }
        
        // Test 3: Comparison operations
        System.out.println("\nTest 3: Comparison Operations");
        try {
            Num n1 = new Num(3);
            Num n2 = new Num(4);
            System.out.println("✓ Num(3) < Num(4) = " + n1.isLessThan(n2));
            System.out.println("✓ Num(3) > Num(4) = " + n1.isGreaterThan(n2));
            System.out.println("✓ Num(3) == Num(4) = " + n1.isEqualTo(n2));
            System.out.println("✓ Num(3) != Num(4) = " + n1.isNotEqualTo(n2));
        } catch (Exception e) {
            System.out.println("✗ Failed: " + e.getMessage());
        }
        
        // Test 4: Error handling - Not a Number
        System.out.println("\nTest 4: Error Handling - Not a Number");
        try {
            Num n = new Num("test");
            System.out.println("✗ Should have thrown exception");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly threw: " + e.getMessage());
        }
        
        // Test 5: Error handling - Out of range (low)
        System.out.println("\nTest 5: Error Handling - Out of Range (Low)");
        try {
            Num n = new Num(0);
            System.out.println("✗ Should have thrown exception");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly threw: " + e.getMessage());
        }
        
        // Test 6: Error handling - Out of range (high)
        System.out.println("\nTest 6: Error Handling - Out of Range (High)");
        try {
            Num n = new Num(11);
            System.out.println("✗ Should have thrown exception");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly threw: " + e.getMessage());
        }
        
        // Test 7: String constructor
        System.out.println("\nTest 7: String Constructor");
        try {
            Num n1 = new Num("5");
            Num n2 = new Num("3.0");
            System.out.println("✓ Created Num from string \"5\": " + n1.toString());
            System.out.println("✓ Created Num from string \"3.0\": " + n2.toString());
        } catch (Exception e) {
            System.out.println("✗ Failed: " + e.getMessage());
        }
        
        // Test 8: Double constructor
        System.out.println("\nTest 8: Double Constructor");
        try {
            Num n1 = new Num(5.0);
            Num n2 = new Num(3.0);
            System.out.println("✓ Created Num from double 5.0: " + n1.toString());
            System.out.println("✓ Created Num from double 3.0: " + n2.toString());
        } catch (Exception e) {
            System.out.println("✗ Failed: " + e.getMessage());
        }
        
        // Test 9: Factory methods
        System.out.println("\nTest 9: Factory Methods");
        try {
            Num n1 = Num.of(7);
            Num n2 = Num.of("8");
            Num n3 = Num.of(9.0);
            System.out.println("✓ Num.of(7) = " + n1.toString());
            System.out.println("✓ Num.of(\"8\") = " + n2.toString());
            System.out.println("✓ Num.of(9.0) = " + n3.toString());
        } catch (Exception e) {
            System.out.println("✗ Failed: " + e.getMessage());
        }
        
        // Test 10: Range validation
        System.out.println("\nTest 10: Range Validation");
        System.out.println("✓ Min value: " + Num.getMinValue());
        System.out.println("✓ Max value: " + Num.getMaxValue());
        System.out.println("✓ Is 5 valid? " + Num.isValidValue(5));
        System.out.println("✓ Is 0 valid? " + Num.isValidValue(0));
        System.out.println("✓ Is 11 valid? " + Num.isValidValue(11));
        
        System.out.println("\n=== All Tests Completed ===");
    }
}
