import os
import re

def get_movie_names(directory):
    movie_names = set()
    pattern = r'(.+?)_frame'
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            match = re.search(pattern, filename)
            if match:
                movie_names.add(match.group(1))
    return movie_names

directory_path1 = 'filter-frame23'
# directory_path1 = 'standard-data/aggregate3/images'
directory_path2 = 'standard-data/valid-second-phase-with-val5-style-transfer/images'
# directory_path2 = 'filter-frame22'

movies_in_dir1 = get_movie_names(directory_path1)
movies_in_dir2 = get_movie_names(directory_path2)

# Finding the duplicated movie names between two directories
duplicated_movies = movies_in_dir1.intersection(movies_in_dir2)

# Printing the count of duplicated movie names
print(f"Number of duplicated movie names: {len(duplicated_movies)}")

# Listing all duplicated movie names
print("List of duplicated movie names:")
for movie_name in duplicated_movies:
    print(movie_name)