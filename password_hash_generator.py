import sys
from werkzeug.security import check_password_hash, generate_password_hash


password_to_hash = sys.argv[1]

print(sys.argv[0],sys.argv[1])

# Save new password
hashAndSalt = generate_password_hash(password_to_hash)

valid = check_password_hash(hashAndSalt, password_to_hash)

print(hashAndSalt)
print(valid)
