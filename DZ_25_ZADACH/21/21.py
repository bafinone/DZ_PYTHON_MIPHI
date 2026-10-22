import re


def is_valid_login(login):
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{3,15}",login))


print(is_valid_login("user_123"))
print(is_valid_login("admin"))
print(is_valid_login("123user"))
print(is_valid_login("ab"))
print(is_valid_login("user-name"))
print(is_valid_login("very_long_username"))
