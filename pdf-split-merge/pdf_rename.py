import os

folder = input("Enter folder path: ")
count = 1

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        os.rename(
            os.path.join(folder, file),
            os.path.join(folder, f"pdf_{count}.pdf")
        )
        count += 1
