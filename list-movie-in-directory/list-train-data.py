import os
import re
from collections import defaultdict
# seems good :) -> actually 1 small bug
def get_unique_movie_names(directory):
    unique_movie_names = defaultdict(str)
    
    # General pattern for matching filename
    general_pattern = r'(.+?)_frame_\d+_out\.jpg$'
    
    episode_patterns = [
        r'Episode \d+', 'tập \d+', 'Tập \d+', 'FULL EPISODE', '--\d+',
        'season \d+', 'Full Episode', r'S\d+ E\d+', r'S\d+E\d+', 
        '-\d+', 'Season \d+', 'Folge \d+', r'Season \d+ Episode \d+ - Part \d+'
    ]
    
    episode_pattern = "|".join(episode_patterns)
    
    for filename in os.listdir(directory):
        general_match = re.fullmatch(general_pattern, filename)
        
        if general_match:
            movie_name = general_match.group(1)
            cleaned_movie_name = re.sub(episode_pattern, '', movie_name).strip()
            
            # Keep an example filename for each unique cleaned movie name
            if not unique_movie_names[cleaned_movie_name]:
                unique_movie_names[cleaned_movie_name] = movie_name
    
    return unique_movie_names

directory_path = 'standard-data/aggregate4/images'

unique_movies_in_dir = get_unique_movie_names(directory_path)
print(f"Number of unique movie names: {len(unique_movies_in_dir)}")
print("List of unique movie names (cleaned name : example filename):")
for cleaned_name, example_filename in unique_movies_in_dir.items():
    print(f"{cleaned_name} : {example_filename}")

