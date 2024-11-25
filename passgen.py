import random
import string

def generate_password(length):
    """
    Generates a random password of specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Character pools
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    special = string.punctuation    # Special characters like !, @, #

    # Ensure password contains at least one character from each category
    all_characters = letters + digits + special
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the characters to randomize their order
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        password = generate_password(password_length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
