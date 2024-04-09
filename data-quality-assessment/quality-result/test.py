import json

# Initialize variables
total_sum = 0
count = 0
json_started = False
json_str_list = []

# Read the file line by line
with open('/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/train-set/upscale-manually-lbl-first-time.json', 'r') as f:
    for line in f:
        # Check if the JSON array has started
        if line.strip() == "[":
            json_started = True

        # If the JSON array has started, append lines to json_str_list
        if json_started:
            json_str_list.append(line.strip())

# Convert list to a single string
json_str = ''.join(json_str_list)

# Load JSON data from the string
try:
    data = json.loads(json_str)
    
    # Iterate through the list and sum the 'mean_score_prediction' values
    for entry in data:
        if 'mean_score_prediction' in entry:
            total_sum += entry['mean_score_prediction']
            count += 1

    # Calculate and print the average
    if count > 0:
        average = total_sum / count
        print(f"The average of 'mean_score_prediction' is: {average}")
        
        # Save the result to a JSON file at the specified path
        result = {'average_mean_score_prediction': average}
        with open('/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/output/train-set/result-of-average-mean_score_prediction-of-upscale-manually-lbl-first-time.json', 'w') as result_file:
            json.dump(result, result_file, indent=4)
            
    else:
        print("No 'mean_score_prediction' found in the data.")
        
except json.JSONDecodeError as e:
    print(f"An error occurred while decoding the JSON: {e}")

