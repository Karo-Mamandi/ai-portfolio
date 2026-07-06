# Outer loop: First number (1 to 10)
for i in range(1, 11):
    # Inner loop: Second number (1 to 10)
    for j in range(1, 11):
        # Print multiplication equation
        print(f"{i} * {j} = {i * j}")
    
    # Print separator line after each row
    print("-" * 10)
