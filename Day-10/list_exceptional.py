import os

folders = input("Please enter the folder names with spaces : ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide the valid folder name")
        continue
    except PermissionError:
        print("No Access to the folder")
        continue

    print("==== Listing the files for the folder - " + folder)

    for file in files:
        print(file)

