import os

def directory_tree():
    """Skilar öllum fælum og subfolders. The whole shebang..."""
    for folder_name, subfolders, filenames in os.walk('C:\\users\\peturdaniel'):
        print(f'Current folder is: {folder_name}')

        for subfolder in subfolders:
            print(f'SUBFOLDER OF {folder_name}: {subfolder}')
        for filename in filenames:
            print(f'FILE INSIDE {folder_name}: {filename}')
        
        print('')

