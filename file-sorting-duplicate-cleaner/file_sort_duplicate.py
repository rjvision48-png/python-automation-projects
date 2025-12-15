import os
import hashlib

folder = input("Enter folder path: ")

seen = {}
duplicates = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if not os.path.isfile(path):
        continue

    with open(path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()

    if file_hash in seen:
        duplicates.append(file)
    else:
        seen[file_hash] = file

print("Duplicate files:")
for d in duplicates:
    print(d)
