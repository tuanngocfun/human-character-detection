import os
import re
from collections import defaultdict

def get_movie_names(directory):
    movie_names = set()
    
    # Define a pattern that matches "data{number}_" at the beginning and ends with "_frame"
    pattern = r'data\d+_(.+?)_frame'
    
    # Go through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            match = re.search(pattern, filename)
            
            # If a match is found, add the core movie name to the set
            if match:
                core_movie_name = match.group(1)
                
                # Remove any episode or series number to consider them as the same movie
                core_movie_name = re.sub(r'_ep\d+|_series\d+', '', core_movie_name)
                
                movie_names.add(core_movie_name)
                
    return movie_names

# directory_path = 'standard-data/aggregate4/images'  
directory_path = 'standard-data/valid-second-phase-with-val5-style-transfer-repair1/images'

# Get the movie names from the specified directory
movies_in_dir = get_movie_names(directory_path)

# Printing the count of unique core movie names
print(f"Number of unique core movie names: {len(movies_in_dir)}")

# Listing all unique core movie names
print("List of unique core movie names:")
for movie_name in movies_in_dir:
    print(movie_name)
