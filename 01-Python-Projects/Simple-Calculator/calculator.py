while True:
    # Get first number from user
    num1 = float(input("please insert the first number: "))

    # Get operator from user - supports +, -, *, /, **(power)
    operation = input("please insert the desired operator among ['+'], ['-'], ['*'], ['/'], ['**']: ")

    # Get second number from user
    num2 = float(input("please insert the second number: "))

    # Check the operator and perform the corresponding operation
    if operation == "+":
        result = num1 + num2  # Addition
    elif operation == "-":
        result = num1 - num2  # Subtraction
    elif operation == "*":
        result = num1 * num2  # Multiplication
    elif operation == "/":
        result = num1 / num2  # Division
    elif operation == "**":
        result = num1 ** num2  # Exponentiation(power)
    else:
        # If operator is not recognized, show error and continue to next loop
        print("The operator inserted by user is wrong!")
        continue  # Skip to next iteration if operator is invalid

    # Display the result
    print(result)
    # Print a separator line for better visual distinction between calculations
    print('---=== End ===---')
