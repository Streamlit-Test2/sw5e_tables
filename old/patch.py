import requests
import json

# API URL for the update endpoint
url = 'https://sw5eapi.azurewebsites.net/api/dataVersion'  # Assume 123 is the user ID

# Headers, possibly including the Content-Type and Origin
headers = {
    'Content-Type': 'application/json',
    'Origin': 'https://sw5e.com'
}
# Send the OPTIONS request
response = requests.options(url)

# Print allowed methods
if 'Allow' in response.headers:
    print("Allowed methods:", response.headers['Allow'])
else:
    print("No 'Allow' header in response.")
# Data to update
# file = open("weaponSupremacy.json")
# data = json.load(file)
# data[0]["name"] = "Blade Supremacys"

# # Convert data to JSON format
# json_data = json.dumps(data)

# # Send the PATCH request
# response = requests.patch(url, headers=headers, data=json_data)

# # Check the response
# if response.status_code == 200:
#     print("Update successful.")
# else:
#     print(f"Failed to update. Status code: {response.status_code}, Response: {response.text}")
