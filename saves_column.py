import pandas as pd

def check_description(description, search_terms):
    for search_term in search_terms:
        if search_term.lower() in str(description).lower():
            return search_term.split()[0]
    return None

# Load the JSON data into a DataFrame
df = pd.read_json('force_data_with_descriptions.json')

# Specify the search term
search_terms = ["Wisdom saving throw", "Strength saving throw", "Dexterity saving throw", "Constitution saving throw", "Intelligence saving throw", "Charisma saving throw"]

# Create a new column 'saves' where you store the search term if it's found in the 'Description'
df['Saves'] = df['Description'].apply(lambda x: check_description(x, search_terms))

# Save the modified DataFrame back to JSON
df.to_json('force_data.json', orient='records')

print("Updated DataFrame:")
print(df)
