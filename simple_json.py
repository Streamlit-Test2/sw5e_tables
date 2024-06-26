import json

def simplify_json(input_filename, output_filename, category="traits"):
    # Open and read the input JSON file
    with open(input_filename, 'r') as file:
        data = json.load(file)
    
    # Extract only the 'name' and 'trait' from each item in the list
    simplified_data = []
    for item in data:
        # Check if both 'name' and 'trait' keys exist in the item
        if 'name' in item and category in item:
            simplified_data.append({
                'name': item['name'],
                category: item[category],
                'type' : "Weapon"
            })
    
    # Write the simplified data to a new JSON file
    with open(output_filename, 'w') as file:
        json.dump(simplified_data, file, indent=4)

# Example usage
simplify_json('weaponProperty.json', 'weaponProperty.json', 'content')
