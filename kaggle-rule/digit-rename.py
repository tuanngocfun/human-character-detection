import os

def rename_files_in_directory(directory_path):
    # List all files in the specified directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    # Sort files to maintain order
    files.sort()
    
    # Iterate through files and enumerate to get a counter value
    for counter, filename in enumerate(files, start=1):
        # Construct the full path to the file
        file_path = os.path.join(directory_path, filename)
        
        # Generate new filename with 5-digit number and .jpg extension
        new_filename = f"{counter:05d}.jpg"
        new_file_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        
        print(f'Renamed "{file_path}" to "{new_file_path}"')

# Usage
directory_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/merge-anime-cartoon-similarity-groups'
rename_files_in_directory(directory_path)

