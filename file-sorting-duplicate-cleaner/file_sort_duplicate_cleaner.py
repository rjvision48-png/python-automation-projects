import os
import shutil
import hashlib

FOLDER = "C:\Users\YourName\Downloads" #  CHANGE YOU FOLDER PATH HERE INSIDE "(WRITE YOUR FOLDER PATH HERE)" 

# FILE SORTING PART 
image_ext = [".jpg", ".jpeg", ".png"]
doc_ext = [".pdf", ".docx"]

images_folder = os.path.join(FOLDER, "Images")
docs_folder = os.path.join(FOLDER, "Documents")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)

for f in os.listdir(FOLDER):
    path = os.path.join(FOLDER, f)

    if os.path.isfile(path):
        if f.lower().endswith(tuple(image_ext)):
            shutil.move(path, os.path.join(images_folder, f))

        elif f.lower().endswith(tuple(doc_ext)):
            shutil.move(path, os.path.join(docs_folder, f))

print("File sorting done.")

# DUPLICATE FINDER PART 
seen = {}
duplicates = []

for f in os.listdir(FOLDER):
    path = os.path.join(FOLDER, f)

    if os.path.isfile(path):
        with open(path, "rb") as file:
            file_hash = hashlib.md5(file.read()).hexdigest()

        if file_hash in seen:
            duplicates.append(f)
        else:
            seen[file_hash] = f

print("\nDuplicate files found:")
for d in duplicates:
    print(d)

print("\nProcess completed successfully.")
