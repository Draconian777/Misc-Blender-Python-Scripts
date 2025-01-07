import os
import shutil

# Prompt the user for mods_dir
mods_dir = input("Please enter the path for the Mods directory: ")

mods_dir_lower = mods_dir.lower()
# Detect if the mods_dir path contains 'win32' or 'win32reboot'

if 'win32reboot' in mods_dir_lower:
    gamefiles_dir = r'H:\PSO2BA\data\win32reboot'
    backup_dir = r'G:\PSO_Stuff\Main Backup\win32reboottemp'
elif 'win32' in mods_dir_lower:
    gamefiles_dir = r'H:\PSO2BA\data\win32'
    backup_dir = r'G:\PSO_Stuff\Main Backup\win32temp'
else:
    # Ask the user to specify the game version if it's not clear from the mods_dir path
    game_version = input("Could not automatically determine the game version from the Mods directory path. Please specify the game version ('win32' or 'win32reboot'): ").strip().lower()
    if game_version == 'win32':
        gamefiles_dir = r'H:\PSO2BA\data\win32'
        backup_dir = r'G:\PSO_Stuff\Main Backup\win32temp'
    elif game_version == 'win32reboot':
        gamefiles_dir = r'H:\PSO2BA\data\win32reboot'
        backup_dir = r'G:\PSO_Stuff\Main Backup\win32reboottemp'
    else:
        print("Invalid choice. Exiting the script.")
        exit()

# 1. Scan "Mods" Directory for all files that are contained within it and its sub-folders
file_list = []
for dirpath, _, filenames in os.walk(mods_dir):
    for filename in filenames:
        # Add the relative path of the file to the list
        file_list.append(os.path.relpath(os.path.join(dirpath, filename), mods_dir))

# 2. Save the list of files into a text file named "listoffiles.txt" in the "backup" directory
os.makedirs(backup_dir, exist_ok=True)  # Ensure backup directory exists
with open(os.path.join(backup_dir, 'listoffiles.txt'), 'w') as f:
    for filepath in file_list:
        f.write(f"{filepath}\n")

# 3. Search for the files listed in the text file within "Gamefiles" Directory
# and copy them to the "Backup" directory
with open(os.path.join(backup_dir, 'listoffiles.txt'), 'r') as f:
    for line in f:
        relative_path = line.strip()
        source_path = os.path.join(gamefiles_dir, relative_path)
        backup_path = os.path.join(backup_dir, relative_path)

        # Ensure the directory structure exists in the Backup directory before copying
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)

        if os.path.exists(source_path):
            shutil.copy2(source_path, backup_path)  # Use copy2 to preserve metadata

print("Operation completed!")
