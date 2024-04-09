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

# directory_path = 'standard-data/aggregate4/images'  
directory_path = 'standard-data/valid-second-phase-with-val5-style-transfer-repair1/images'

# Get the movie names from the specified directory
movies_in_dir = get_movie_names(directory_path)

# Printing the count of movie names
print(f"Number of movie names: {len(movies_in_dir)}")

# Listing all movie names
print("List of movie names:")
for movie_name in movies_in_dir:
    print(movie_name)
