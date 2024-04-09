import os

def rename_files(directory):
    for filename in sorted(os.listdir(directory)):
        # Ensure we're only processing .jpg files
        if filename.endswith(".jpg"):
            # Extract the old index from the filename
            old_index = int(filename.split('.')[0])
            # Calculate the new index
            new_index = old_index + 30193
            # Create the new filename
            new_filename = f"{new_index:05d}.jpg"
            # Construct the full paths for old and new filenames
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_filepath, new_filepath)
        else:
            print(f"Skipping non-jpg file: {filename}")

# Define the directory path
directory_path = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/merge-anime-cartoon-similarity-groups'

# Call the function to rename files
rename_files(directory_path)
