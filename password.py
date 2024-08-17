import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Generate a random password with the specified length and character types."""
    
    # Define the possible character sets
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    """Main function to interact with the user and generate a password."""
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired password length (default 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()