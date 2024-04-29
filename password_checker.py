import re


def check_password_strength(password):
    """
    Checks the strength of a password based on various criteria.

    Args:
    - password (str): The password to be checked.

    Returns:
    - strength (str): Feedback on the password's strength.
    """
    length = len(password)
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_number = bool(re.search(r'[0-9]', password))
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if length < 8:
        return "Weak: Password should be at least 8 characters long."
    elif not has_lowercase:
        return "Weak: Password should contain lowercase letters."
    elif not has_uppercase:
        return "Weak: Password should contain uppercase letters."
    elif not has_number:
        return "Weak: Password should contain numbers."
    elif not has_special_char:
        return "Weak: Password should contain special characters."
    else:
        return "Strong: Password meets all complexity criteria."


# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)
