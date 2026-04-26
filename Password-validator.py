import re

def is_secure_password(password):
    """Checks if a password meets business security standards."""
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

# Test cases
test_pw = "DevSolutions2026!"
print(f"Security Audit for '{test_pw}': {'PASS' if is_secure_password(test_pw) else 'FAIL'}")
