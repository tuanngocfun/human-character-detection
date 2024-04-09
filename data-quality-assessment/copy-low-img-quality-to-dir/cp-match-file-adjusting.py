import json
import os
import shutil
import re

# Define the path to the JSON file and image directory
json_file_path = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/merge-anime-cartoon-similarity-groups.json"
image_dir_path = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/merge-anime-cartoon-similarity-groups"

# Define the target directory
target_dir_path = "/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/low-mean-score-image-quality/merge-cartoon-anime-similarity-groups"

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir_path):
    os.makedirs(target_dir_path)

# Load JSON data
json_content = ""
with open(json_file_path, "r") as f:
    file_content = f.read()
    
    # Use a regex to find the first correct JSON syntax (starts from an open square bracket followed by an open curly bracket)
    match = re.search(r'\[\s*{', file_content)
    
    if match:
        json_content = file_content[match.start():]  # get the content from matched position to end

# Load content into a JSON object
json_data = json.loads(json_content)

# Iterate through the JSON objects
for entry in json_data:
    image_id = entry.get("image_id", None)
    mean_score_prediction = entry.get("mean_score_prediction", None)

    if image_id is not None and mean_score_prediction is not None:
        # Check if mean_score_prediction is lower than 5
        if mean_score_prediction < 5:
            image_id_str = str(image_id).zfill(5) + ".jpg"

            source_image_path = os.path.join(image_dir_path, image_id_str)
            target_image_path = os.path.join(target_dir_path, image_id_str)

            # Check if the corresponding image exists and copy it to the target directory
            if os.path.exists(source_image_path):
                shutil.copy(source_image_path, target_image_path)
                print(f"Copied {image_id_str} to {target_dir_path}")
