import os
import re

def extract_and_clean_movie_names(directory):
    unique_movie_names = {}  # Dictionary to store unique movie names

    for filename in os.listdir(directory):
        match_a = re.search(r'(data\d+)_(.*?)_', filename)
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

def find_common_movies(src_directory, tgt_directory):
    src_movies = extract_and_clean_movie_names(src_directory)
    tgt_movies = extract_and_clean_movie_names(tgt_directory)
    
    common_movies = set(src_movies.keys()).intersection(set(tgt_movies.keys()))
    return common_movies

if __name__ == "__main__":
    src_directory = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4/images'
    tgt_directory = '/media/ngoc/a normal usb/ngoc/new-val/valid-second-phase-with-val5-style-transfer-repair/images'

    if os.path.exists(src_directory) and os.path.exists(tgt_directory):
        common_movies = find_common_movies(src_directory, tgt_directory)
        
        print(f"Common movie names:")
        for movie in common_movies:
            print(f"Movie: {movie}")
        
        print(f"Number of common movie names: {len(common_movies)}")
    else:
        print(f"One of the directories does not exist.")

