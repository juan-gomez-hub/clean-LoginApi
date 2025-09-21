import re
from app.exceptions.user_exceptions import thisUserNotExist


def validateUsername(username,login=False):
        username=username
        if not username or len(username.strip()) == 0:
            raise ValueError("Username cannot be empty")
        if len(username) > 30 or len(username) < 5:
            if not login:
                raise ValueError("Username must be between 5 and 30 characters")
            else:
                raise  thisUserNotExist
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        return username.strip()
        

def validationEmail(email):
    if not email or len(email.strip()) == 0:
            raise ValueError("Email cannot be empty")
    if len(email) > 100:
            raise ValueError("Email must be under 100 characters")
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
    return email.strip().lower()

def validationPassword(password):
    # Validate and hash password
    if not password or len(password.strip()) == 0:
            raise ValueError("Password cannot be empty")
    if len(password) > 30 or len(password) < 8:  # Increased minimum to 8 for security
            raise ValueError("Password must be between 8 and 30 characters")
    return password