import os
import glob
import re
from concurrent.futures import ThreadPoolExecutor

def check_comparison_directories(comp_dir):
    try:
        return os.listdir(comp_dir)
    except FileNotFoundError:
        print(f"Directory not found: {comp_dir}")
    except PermissionError:
        print(f"Permission denied for directory: {comp_dir}")
    return []

def check_duplicate_files(destination_directory, comparison_directories):
    # Accumulate comparison files from all directories using parallel processing
    comparison_files = set()
    with ThreadPoolExecutor() as executor:
        for files in executor.map(check_comparison_directories, comparison_directories):
            comparison_files.update(files)

    # Attempt to list files in the destination directory
    try:
        destination_files = os.listdir(destination_directory)
    except FileNotFoundError:
        print(f"Destination directory not found: {destination_directory}")
        return
    except PermissionError:
        print(f"Permission denied for destination directory: {destination_directory}")
        return

    # Check for duplicates
    duplicates = [file for file in destination_files if file in comparison_files]
    if duplicates:
        print(f"Duplicated files found: {', '.join(duplicates)}")
    else:
        print("No duplicated files found.")

# Pattern and comparison_directories
pattern = '../../filter-vid*'
comparison_directories = [folder for folder in glob.glob(pattern) if os.path.isdir(folder)]

# Extract numbers related to directories using regular expressions
directory_numbers = [
    int(re.search(r'filter-vid(\d+)', folder).group(1)) if re.search(r'filter-vid(\d+)', folder) else -1
    for folder in comparison_directories
]

# Find the highest number
max_number = max(directory_numbers)

# Set the destination directory to the highest number
destination_directory = f'../../filter-vid{max_number}'

# Remove the directory with the highest number from the comparison directories
comparison_directories = [folder for folder in comparison_directories if not folder.endswith(str(max_number))]

# Find the second highest number and filter comparison directories
second_max_number = max([num for num in directory_numbers if num != max_number])
comparison_directories = [folder for folder in comparison_directories if folder.endswith(str(second_max_number))]

# Call the function to check for duplicates
check_duplicate_files(destination_directory, comparison_directories)