import sys
from classes.PasswordHelper import PasswordHelper


password_to_hash = sys.argv[0]

hashed = PasswordHelper.get_hashed_password(password_to_hash)

is_match = PasswordHelper.check_password(sys.argv[0],hashed)

print(hashed)
print(is_match)