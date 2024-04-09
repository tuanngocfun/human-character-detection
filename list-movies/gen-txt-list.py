import os

# Base directory path
base_path = '/media/ngoc/a normal usb/ngoc-data-thesis/videos'

# List of directories to search for
directories = ['train', 'val', 'test', 'test2']

# Output file to write the movie list
output_file = os.path.join(base_path, 'movie-list-in-dataset.txt')

# Function to recursively search for .mp4 files in the given directory
def find_mp4_files(directory):
    movies = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.mp4'):
                movies.append(os.path.join(dirpath, filename))
    return movies

# Collect all movie file paths
all_movies = []
for directory in directories:
    dir_path = os.path.join(base_path, directory)
    all_movies.extend(find_mp4_files(dir_path))

# Write movie file paths to the output file
with open(output_file, 'w') as f:
    for movie in all_movies:
        f.write(movie + '\n')

print(f"List of movies written to {output_file}")
