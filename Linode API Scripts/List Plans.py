import requests

# Set the API endpoint
endpoint = "https://api.linode.com/v4/linode/types"

# Set the API key in the header
headers = {
    "Authorization": "Bearer API-KEY"
}

# Make a GET request to the endpoint
response = requests.get(endpoint, headers=headers)

# Print the raw response text
print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Loop through the list of Linode Types and print the name and price
    for linode_type in data['data']:
        print(f"{linode_type['label']}: ${linode_type['price']['monthly']}/month")
else:
    # Print an error message if the request was unsuccessful
    print(f"Request failed with status code {response.status_code}")
