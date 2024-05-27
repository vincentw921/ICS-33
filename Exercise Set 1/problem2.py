import hashlib

with open("./problem1.py", mode='rb') as file:
    print(hashlib.file_digest(file, "sha256"))