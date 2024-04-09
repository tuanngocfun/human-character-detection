import os
import re
from collections import defaultdict

def extract_and_clean_movie_names(directory):
    unique_movie_names = {}
    
    for filename in os.listdir(directory):
        match = re.search(r'(data\d+)_([\w.]+)--', filename)
        
        if match:
            data_number = match.group(1)
            movie_name = match.group(2)
            
            # Replace underscores and special characters with spaces for a cleaner movie name
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
