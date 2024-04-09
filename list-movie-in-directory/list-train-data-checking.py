import os
import re
from collections import defaultdict

def get_unique_movie_names(directory):
    unique_movie_names = defaultdict(str)
    
    # General pattern for matching filename
    general_pattern = r'(.+?)_frame_\d+_out\.jpg$'
    
    # Patterns related to episodes, seasons, parts, etc.
    episode_patterns = [
        r'Episode \d+', r'tập \d+', r'Tập \d+', r'FULL EPISODE', r'--\d+',
        r'season \d+', r'Full Episode', r'S\d+ E\d+', r'S\d+E\d+', 
        r'-\d+', r'Season \d+', r'Folge \d+', r'Season \d+ Episode \d+ - Part \d+'
    ]
    
    episode_pattern = re.compile("|".join(episode_patterns))
    
    for filename in os.listdir(directory):
        general_match = re.fullmatch(general_pattern, filename)
        
        if general_match:
            movie_name = general_match.group(1)
            cleaned_movie_name = episode_pattern.sub('', movie_name).strip()
            
            # Keep an example filename for each unique cleaned movie name
            if cleaned_movie_name not in unique_movie_names:
                unique_movie_names[cleaned_movie_name] = movie_name
    
    return unique_movie_names

directory_path = 'standard-data/aggregate4/images'

unique_movies_in_dir = get_unique_movie_names(directory_path)
print(f"Number of unique movie names: {len(unique_movies_in_dir)}")
print("List of unique movie names (cleaned name : example filename):")
for cleaned_name, example_filename in unique_movies_in_dir.items():
    print(f"{cleaned_name} : {example_filename}")

