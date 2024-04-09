import os

def sanitize_filename(filename):
    # Define the set of allowed characters based on Kaggle's rules
    # Assuming that letters, digits, and underscores are allowed
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    
    # Remove any disallowed characters from the filename
    sanitized_filename = ''.join(c for c in filename if c in allowed_characters)
    
    # Optionally, add any additional sanitization logic here
    
    return sanitized_filename

def sanitize_filenames_in_directory(directory_path):
    # List all files in the specified directory
    for filename in os.listdir(directory_path):
        # Construct the full path to the file
        file_path = os.path.join(directory_path, filename)
        
        # Skip subdirectories
        if os.path.isdir(file_path):
            continue
        
        # Sanitize the filename
        sanitized_filename = sanitize_filename(filename)
        
        # Construct the full path to the sanitized file
        sanitized_file_path = os.path.join(directory_path, sanitized_filename)
        
        # Rename the file
        os.rename(file_path, sanitized_file_path)
        
        print(f'Renamed "{file_path}" to "{sanitized_file_path}"')

# Usage
directory_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-cartoon/combine-cartoon'
sanitize_filenames_in_directory(directory_path)

