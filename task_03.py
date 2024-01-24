import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    password_length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Error: Please enter a valid number for password length.")
    exit()

# Generate and display the password
if password_length > 0:
    password = generate_password(password_length)
    print(f"Generated Password: {password}")
else:
    print("Error: Password length must be greater than 0.")
