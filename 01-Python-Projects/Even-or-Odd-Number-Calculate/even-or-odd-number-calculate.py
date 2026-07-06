# Ask user for a number and store it
num = int(input("please insert The number: "))

# Check if number divided by 2 has no remainder (even number)
if num % 2 == 0:
    print("The number is an even number.")  # Tell user it's even
else:
    print("The number is an odd number.")   # Tell user it's odd
