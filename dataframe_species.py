import json
import pandas as pd
import re

def json_to_dataframe(input_filename):
    # Open and read the input JSON file
    with open(input_filename, 'r') as file:
        data = json.load(file)

    # Prepare data for the DataFrame
    processed_data = []
    for item in data:
        name = item.get('name', '')
        #print(name)
        traits = item.get('traits', [])
        speed = None
        alignment = None
        simplified_traits = []
        armor = False
        primary_boost = None
        secondary_boost = None
        for trait in traits[5:]:
            if trait['name'] not in ["Type", "Languages"]:
                simplified_traits.append(trait["name"])
        for trait in traits:  
            if "armor" in trait.get("description", "").lower():
                armor = True  
            if trait["name"] == "Speed":
                speed_str = trait["description"]
                # Assuming the speed is always in mph and we convert it to feet per second (fps)
                # Conversion factor: 1 mph = 1.46667 fps
                match = re.search(r'(\d+)', speed_str)
                if match:
                    speed = match.group(0) + " ft"
                else:
                    speed = None  # If no number is found
            if trait["name"] == "Alignment":
                description = trait["description"]
                # Regex to find alignment words
                matches = re.findall(r'\b(dark|light|chaotic|lawful|balanced|chaos)\b', description, re.IGNORECASE)
                if matches:
                    alignment = []
                    for x in matches: 
                        if x == "chaos":
                            x = "chaotic"
                        alignment.append(x.capitalize())
                else:
                    alignment = ["Any"]

            if trait["name"] == "Ability Score Increase":
                # Specific boosts
                specific_boosts = re.findall(r'(\w+) score increases by (\d)', trait["description"])
                if specific_boosts:
                    specific_boosts.sort(key=lambda x: int(x[1]), reverse=True)
                    primary_boost = specific_boosts[0] if len(specific_boosts) > 0 else None
                    secondary_boost = specific_boosts[1:] if len(specific_boosts) > 1 else None

                # Generic boosts
                if primary_boost == None:
                    if name == "Human" or name == "Half-human":
                        primary_boost = "your_choice"
                    elif name == "Massassi":
                        primary_boost = "Constitution"
                    else:
                        primary_boost = None
                        secondary_boost = ["3 stats"]
                else:
                    primary_boost = primary_boost[0]
                if secondary_boost == None:
                    secondary_boost = ["your_choice"]
                else:
                    secondary_boost = [x[0] for x in secondary_boost]
                    if secondary_boost == ["3"]:
                        secondary_boost = ["Typo"]

        processed_data.append({
            'Name': name,
            'Primary' : primary_boost,
            'Secondary': secondary_boost,
            'Speed': speed,
            'Alignment' : alignment,
            'Armor': armor,
            'Traits': simplified_traits,
        })

    # Create DataFrame
    df = pd.DataFrame(processed_data)
    return df

# Example usage
df = json_to_dataframe('species_data.json')
df.to_json("species_df.json", orient='records')

print(df)
