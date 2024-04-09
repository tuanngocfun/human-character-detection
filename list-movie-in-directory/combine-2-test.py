import os
import re
from collections import defaultdict

def extract_and_clean_movie_names(directory):
    unique_movie_names = {}  # Dictionary to store unique movie names

    for filename in os.listdir(directory):
        # Check for matches using regular expressions from both code snippets
        match_a = re.search(r'(data\d+)_(.*?)_', filename)
        # Updated regex to include hyphen '-' along with word characters and dots
        match_b = re.search(r'(data\d+)_([\w.-]+)--', filename)

        if match_a:
            data_number = match_a.group(1)
            movie_name = match_a.group(2)

            cleaned_movie_name = re.sub(r'[-\d]+$', '', movie_name)

            if unique_movie_names.get(cleaned_movie_name) is None:
                unique_movie_names[cleaned_movie_name] = movie_name

        if match_b:
            data_number = match_b.group(1)
            movie_name = match_b.group(2)

            cleaned_movie_name = re.sub(r'[_-]', ' ', movie_name)
            
            if cleaned_movie_name not in unique_movie_names:
                unique_movie_names[cleaned_movie_name] = movie_name

    return unique_movie_names

if __name__ == "__main__":
    directory = 'standard-data/aggregate4/images'

    if os.path.exists(directory):
        unique_movie_names = extract_and_clean_movie_names(directory)

        for cleaned, original in unique_movie_names.items():
            print(f"Movie name: {original}, Cleaned: {cleaned}")

        print(f"Number of unique movie names: {len(unique_movie_names)}")
    else:
        print(f"The directory '{directory}' does not exist.")
