# Get base number from user input and convert to integer
base = int(input("Enter the base: "))

# Get power/exponent from user input and convert to integer
power = int(input("Enter the power: "))

def compute_power(base, power):
    """
    Calculate base raised to the power using iterative multiplication.
    
    Parameters:
    base (int): The base number
    power (int): The exponent (non-negative integer)
    
    Returns:
    int: The result of base^power
    """
    # Initialize result to 1 (identity element for multiplication)
    result = 1
    
    # Loop 'power' times, multiplying result by base each iteration
    # This simulates base * base * base ... (power times)
    for x in range(power):
        result = result * base  # Multiply current result by base
    
    # Return the final computed value
    return result

# Call the function with user inputs and print the result
print(compute_power(base, power))
