import os

def list_files_in_paths(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Access Denied"
    
def main():
    folder_paths = input("please Provide the folder name with spaces in b/w :").split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_paths(folder_path)
        if files:
            print(f"Files in {folder_path}")
            for file in files:
                print(file)
        
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == main():
    main
