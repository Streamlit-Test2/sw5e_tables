import pandas as pd

def check_description(description, search_terms):
    for search_term in search_terms:
        if search_term.lower() in str(description).lower():
            return search_term.split()[0]
    return None

# Load the JSON data into a DataFrame
df = pd.read_json('force_data_with_descriptions.json')

# Specify the search term
search_terms = ["Acid damage", "Cold damage", "Energy damage", "Fire damage", "Force damage", "Ion damage", "Kinetic damage", "Lightning damage", "Necrotic damage","Poison damage", "Psychic damage", "Sonic damage", "True damage"]

# Create a new column 'saves' where you store the search term if it's found in the 'Description'
df['DType'] = df['Description'].apply(lambda x: check_description(x, search_terms))

# Save the modified DataFrame back to JSON
df.to_json('force_data.json', orient='records')

print("Updated DataFrame:")
print(df)
