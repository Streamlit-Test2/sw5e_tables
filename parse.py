from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML file
with open('force.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the first table
table = soup.find('table')
for nested in table.find_all('table'): #get rid of the tables within
    nested.decompose()
# Extract table data using pandas
df = pd.read_html(str(table))[0]
#print(df)
# Initialize a list for descriptions
descriptions = [None] * len(df)

# Iterate through each row in the table
for i, td in enumerate(table.find_all('td', class_='pt-3', colspan='9')):
    # Extract all text from the div within this td
    if td.div:
        descriptions[i]= td.div.get_text(strip=True)
    else:
        descriptions[i] = "No description available"  # Fallback if no div is found

# Add descriptions as a new column to the DataFrame
#print(descriptions)
df['Description'] = descriptions

# Save the table data as a JSON file
file_path = 'force_data_with_descriptions.json'
df.to_json(file_path, orient='records')

print(f"Table data with descriptions saved as JSON: {file_path}")
print(df)
