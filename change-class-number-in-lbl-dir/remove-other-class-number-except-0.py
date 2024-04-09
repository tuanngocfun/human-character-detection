import os

def process_txt_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            
            # Read the file into memory
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Keep lines where the label class is '0'
            filtered_lines = [line for line in lines if line.startswith('0 ')]
            
            # Write the filtered lines back into the file
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
            
            # Check if the file is empty, if yes then remove it
            if os.path.getsize(file_path) == 0:
                os.remove(file_path)

# Specify the directory where the .txt label files are stored
directory_path = '/media/ngoc/mydisk/ngoc/thesis/dataset/aggregate4/labels'

process_txt_files(directory_path)

