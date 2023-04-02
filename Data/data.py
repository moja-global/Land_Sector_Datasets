import json

# Read in the JSON data
with open('KEN_AL2_Kenya_GEZ.json', 'r') as f:
    data = json.load(f)

# Process the data
processed_data = []
for item in data:
    # Perform some transformation on the data
    processed_item = {
        'name': item['name'],
        'age': item['gez_code'] * 2
    }
    processed_data.append(processed_item)

# Write the processed data to a new JSON file
with open('processed_data.json', 'w') as f:
    json.dump(processed_data, f)
