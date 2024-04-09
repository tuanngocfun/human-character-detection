import os
import re
from collections import defaultdict

def extract_and_clean_movie_names(directory):
    unique_movie_names = {}  # Changed from defaultdict(str)

    for filename in os.listdir(directory):
        match = re.search(r'(data\d+)_(.*?)_', filename)
        if match:
            data_number = match.group(1)
            movie_name = match.group(2)

            cleaned_movie_name = re.sub(r'[-\d]+$', '', movie_name)  # Simplified the pattern
            
            # Checking if cleaned_movie_name exists in unique_movie_names
            if unique_movie_names.get(cleaned_movie_name) is None:
                unique_movie_names[cleaned_movie_name] = movie_name
    
    return unique_movie_names

if __name__ == "__main__":
    directory = 'standard-data/aggregate4/images'
    
    if os.path.exists(directory):  # Checking if the directory exists
        unique_movie_names = extract_and_clean_movie_names(directory)
        for cleaned, original in unique_movie_names.items():
            print(f"Movie name: {original}, Cleaned: {cleaned}")
        print(f"Number of unique movie names: {len(unique_movie_names)}")
    else:
        print(f"The directory '{directory}' does not exist.")
