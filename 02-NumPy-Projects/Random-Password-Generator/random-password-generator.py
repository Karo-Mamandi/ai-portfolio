# Generating random passwords with NumPy
# Idea: Create a password by randomly selecting characters.

import numpy as np

# Create array of allowed characters (letters, numbers, and *)
chars = np.array(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*"))

# Randomly select 12 characters and join them into a string
password = ''.join(np.random.choice(chars, size=12))

# Display the character set and generated password
print(chars)
print("Random Password: ", password)
