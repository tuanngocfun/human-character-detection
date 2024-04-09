import os
import glob

def remove_txt_files(directory_path):
    # Check if the given path is a valid directory
    if not os.path.isdir(directory_path):
        print(f"The path {directory_path} is not a valid directory.")
        return
    
    # Create a pattern to match all .txt files in the given directory
    pattern = os.path.join(directory_path, '*.txt')
    
    # Use the glob module to find all the matching files
    txt_files = glob.glob(pattern)
    
    # Loop through the files and remove them
    for file in txt_files:
        try:
            os.remove(file)
            print(f"Successfully removed {file}")
        except OSError as e:
            print(f"Error removing {file}: {str(e)}")

# Example usage
directory_path = '/home/aivn12gb/yolov8_domain_adaption_evn/data/new-val/labels' 
remove_txt_files(directory_path)
