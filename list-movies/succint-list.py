import os

base_directory = '/media/ngoc/a normal usb/ngoc-data-thesis/videos'
output_file_path = os.path.join(base_directory, 'movie-list-in-dataset.txt')

with open(output_file_path, 'w') as f:
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.mp4'):
                # Remove the base directory from the path before writing to the file
                relative_path = os.path.relpath(os.path.join(root, file), base_directory)
                f.write(relative_path + '\n')

print(f"List of movies written to: {output_file_path}")
