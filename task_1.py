
import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return False
    
    # Uppercase
    if not re.search(r"[A-Z]", password):
        return False
    
    # Lowercase
    if not re.search(r"[a-z]", password):
        return False
    
    # Digit
    if not re.search(r"[0-9]", password):
        return False
    
    # Special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True


# MAIN SCRIPT
if __name__ == "__main__":
    pwd = input("Enter your password: ")

    if check_password_strength(pwd):
        print("Password is strong!")
    else:
        print("Weak password! Please include uppercase, lowercase, numbers, and special characters.")
