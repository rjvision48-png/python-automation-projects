import os

folder = input("Enter folder path: ")
count = 1

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):
        new_name = f"file_{count}.{file.split('.')[-1]}"
        os.rename(path, os.path.join(folder, new_name))
        count += 1
