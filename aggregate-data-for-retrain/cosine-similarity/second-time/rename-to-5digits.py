import os

images_directory = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/second-time/images'
labels_directory = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/second-time/labels'

def generate_mapping(directory, file_extension):
    mapping = {}
    for counter, filename in enumerate(sorted(os.listdir(directory)), start=1):
        if filename.endswith(file_extension):
            new_filename = f"{counter:05d}"
            # Get the old filename without the extension
            old_filename = os.path.splitext(filename)[0]
            # Store the mapping of old to new filename
            mapping[old_filename] = new_filename
    return mapping

def rename_files(directory, file_extension, mapping):
    for filename in os.listdir(directory):
        # Get the old filename without the extension
        old_filename = os.path.splitext(filename)[0]
        # Check if the old filename is in the mapping
        if old_filename in mapping:
            # Build the new filename using the mapping and file extension
            new_filename = f"{mapping[old_filename]}{file_extension}"
            # Get the full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the files
            os.rename(old_file, new_file)
            print(f"Renamed {old_file} to {new_file}")

filename_mapping = generate_mapping(images_directory, '.jpg')

rename_files(images_directory, '.jpg', filename_mapping)
rename_files(labels_directory, '.txt', filename_mapping)

print("All file renaming is complete.")
