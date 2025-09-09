# Your code here
import re

def valid_password(n):

    if not re.search(r'[a-z]', n):
        return 'Invalid password. Please try again'
    if not re.search(r'[A-Z]', n):
        return 'Invalid password. Please try again'
    if not re.search(r'[0-9]', n):
        return 'Invalid password. Please try again'
    if not re.search(r'[$#@]', n):
        return 'Invalid password. Please try again'
    if len(n) < 6 or len(n) > 12:
        return 'Invalid password. Please try again'

    return "Valid password"

print(valid_password("ABd1234@1"))