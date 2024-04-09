import os
import re
# this code is not correct???
def get_unique_movie_names(directory):
    unique_movie_names = set()
    
    # This pattern captures text between 'data\d+_' and '_frame_\d+\.jpg'
    general_pattern = r'data\d+_(.+?)_frame_\d+\.jpg$'
    
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
            cleaned_movie_name = re.sub(episode_pattern, '', movie_name)
            unique_movie_names.add(cleaned_movie_name.strip())
    
    return unique_movie_names

directory_path = 'standard-data/aggregate4/images'  # Update this path as needed

unique_movies_in_dir = get_unique_movie_names(directory_path)
print(f"Number of unique movie names: {len(unique_movies_in_dir)}")
print("List of unique movie names:")
for movie_name in unique_movies_in_dir:
    print(movie_name)
