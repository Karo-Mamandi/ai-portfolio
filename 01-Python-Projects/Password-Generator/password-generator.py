# Import secrets for cryptographically secure random numbers
# Import string for character sets (letters, digits, etc.)
import secrets
import string


def generate_password(length=12, use_upper=True, use_lower=True,
                      use_digits=True, use_special=True):
    """Generate a secure password with customizable options.

    Args:
        length (int): Desired password length (default: 12)
        use_upper (bool): Include uppercase letters (default: True)
        use_lower (bool): Include lowercase letters (default: True)
        use_digits (bool): Include digits (default: True)
        use_special (bool): Include special characters (default: True)

    Returns:
        str: Generated password
    """

    # Build character pool based on selected options
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase  # a-z
    if use_upper:
        chars += string.ascii_uppercase  # A-Z
    if use_digits:
        chars += string.digits  # 0-9
    if use_special:
        chars += "!@#$%&*"  # Special characters

    # Ensure at least one character from each selected set
    password = []
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_special:
        password.append(secrets.choice("!@#$%&*"))

    # Fill remaining length with random characters from the pool
    remaining = length - len(password)
    password.extend(secrets.choice(chars) for _ in range(remaining))

    # Shuffle to avoid predictable patterns (e.g., all special chars at start)
    secrets.SystemRandom().shuffle(password)

    # Convert list to string and return
    return ''.join(password)


# Get password length from user
length = int(input("Enter Password length: "))

# Generate password with default settings
password = generate_password(length)

# Display results
print(f"Generated Password: {password}")
# Approximate entropy calculation: 4 bits per character (average for mixed character set)
print(f"Password Strength: {len(password) * 4} bits")  # Approximate entropy
