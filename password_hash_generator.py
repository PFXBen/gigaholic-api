import sys
from passlib.hash import pbkdf2_sha256


password_to_hash = sys.argv[0]

hashed = pbkdf2_sha256.hash(str(sys.argv[0]))

is_match = pbkdf2_sha256.verify(sys.argv[0],hashed)

print(hashed)
print(is_match)