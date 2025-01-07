import os
import shutil

def find_largest_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and len(f) == 32]
    if len(files) < 2:
        raise ValueError("Not enough files in the directory to compare.")
    file_sizes = {file: os.path.getsize(os.path.join(directory, file)) for file in files[:2]}
    sorted_files = sorted(file_sizes, key=file_sizes.get, reverse=True)
    return sorted_files[0], sorted_files[1]

def create_folder(directory, folder_name):
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    return folder_path

def move_files_to_folder(files, source_dir, target_folder):
    for file in files:
        os.rename(os.path.join(source_dir, file), os.path.join(target_folder, file))

def move_files_up_and_remove_group(directory):
    for file in os.listdir(directory):
        shutil.move(os.path.join(directory, file), os.path.dirname(directory))
    os.rmdir(directory)

def main():
    directory = input("Please enter the path of the main directory: ")
    if not os.path.isdir(directory):
        print("The specified path does not exist or is not a directory.")
        return

    base_name, secondary_name = find_largest_files(directory)
    ori_folder = create_folder(directory, "ori")
    modded_folder = create_folder(directory, "Modded")

    # Move the original files to the 'ori' folder
    move_files_to_folder([base_name, secondary_name], directory, ori_folder)

    ext_folder = f"{base_name}_ext"
    ext_directory = os.path.join(directory, ext_folder)
    group2_directory = os.path.join(ext_directory, "group2")
    if not os.path.exists(group2_directory):
        raise ValueError(f"Group2 directory '{group2_directory}' does not exist.")

    # Finding the .aqp file in the group2 folder
    aqp_file = None
    for file in os.listdir(group2_directory):
        if file.endswith('.aqp'):
            aqp_file = file
            break

    if not aqp_file:
        raise ValueError("No .aqp file found in the group2 directory.")

    # Move files from group2 up one level and remove the group2 folder
    move_files_up_and_remove_group(group2_directory)

    # Generate the first batch file zzz.bat
    with open(os.path.join(directory, "zzz.bat"), 'w') as file:
        file.write(
            "@echo off\n"
            "REM Change directory to the location of the source file\n"
            f"cd /d \"{directory}\"\n\n"
            "REM Rename the file\n"
            f"rename \"Final_out.aqp\" \"{aqp_file}\"\n\n"
            "REM Move the renamed file to the target directory and overwrite if necessary\n"
            f"move /y \"{aqp_file}\" \"{os.path.join(directory, ext_folder)}\"\n"
        )

    # Generate the second batch script for copying and moving files
    with open(os.path.join(directory, "xxx.bat"), 'w') as file:
        file.write(
            "@echo off\n"
            ":: Define file paths\n"
            f"set sourceFile=\"{base_name}_ext.ice\"\n"
            f"set targetFile1=\"{base_name}\"\n"
            f"set targetFile2=\"{secondary_name}\"\n"
            f"set destinationFolder=\"{os.path.join(directory, 'Modded')}\"\n\n"
            ":: Rename the original file\n"
            "rename %sourceFile% %targetFile1%\n\n"
            ":: Copy the renamed file to create the second one\n"
            "copy %targetFile1% %targetFile2%\n\n"
            ":: Move both files to the destination folder, overwrite if they already exist\n"
            "move /Y %targetFile1% %destinationFolder%\n"
            "move /Y %targetFile2% %destinationFolder%\n\n"
            ":: Notify completion\n"
            "echo Files have been renamed, copied, and moved successfully.\n"
        )
        # Generate the third batch script www.bat
    with open(os.path.join(directory, "www.bat"), 'w') as file:
        file.write(
            "@echo off\n"
            f":: Define the specific files to copy\n"
            f"set baseFile=\"{os.path.join(directory, 'Modded', base_name)}\"\n"
            f"set secondaryFile=\"{os.path.join(directory, 'Modded', secondary_name)}\"\n"
            ":: Define the game data directory\n"
            "set gameDataFolder=\"G:\\Epic Games\\PHANTASYSTARONLINE2_NA\\pso2_bin\\data\\win32\"\n\n"
            ":: Copy the specific files to the game data directory\n"
            "echo Copying {base_name}...\n"
            "copy %baseFile% %gameDataFolder% /Y\n"
            "echo Copying {secondary_name}...\n"
            "copy %secondaryFile% %gameDataFolder% /Y\n"
            "echo Files have been copied to the game directory successfully.\n"
        )
    with open(os.path.join(directory, "vvv.bat"), 'w') as file:
        file.write(
            "@echo off\n"
            f":: Define the specific files to copy\n"
            f"set baseFile=\"{os.path.join(directory, 'ori', base_name)}\"\n"
            f"set secondaryFile=\"{os.path.join(directory, 'ori', secondary_name)}\"\n"
            ":: Define the game data directory\n"
            "set gameDataFolder=\"G:\\Epic Games\\PHANTASYSTARONLINE2_NA\\pso2_bin\\data\\win32\"\n\n"
            ":: Copy the specific files to the game data directory\n"
            "echo Copying {base_name}...\n"
            "copy %baseFile% %gameDataFolder% /Y\n"
            "echo Copying {secondary_name}...\n"
            "copy %secondaryFile% %gameDataFolder% /Y\n"
            "echo Files have been copied to the game directory successfully.\n"
        )


if __name__ == "__main__":
    main()
