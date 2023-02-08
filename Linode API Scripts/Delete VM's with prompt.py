import requests
import json

# API key for authentication
api_key = "PUT-API-KEY-HERE"

# API endpoint for getting a list of instances
instances_endpoint = "https://api.linode.com/v4/linode/instances"

# API endpoint for deleting an instance
delete_instance_endpoint = "https://api.linode.com/v4/linode/instances/{}"

# Headers for API request
headers = {
    "Authorization": "Bearer {}".format(api_key),
    "Content-Type": "application/json"
}

# Get a list of instances
response = requests.get(instances_endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    instances = response.json()["data"]
    
    # Print the list of instances and ask the user to select one for deletion
    for i, instance in enumerate(instances):
        print("[{}] {} ({})".format(i+1, instance["label"], instance["id"]))
    
    selected_instance = int(input("Enter the number of the instance you want to delete: ")) - 1
    instance_id = instances[selected_instance]["id"]
    
    # Confirm with the user if they really want to delete the selected instance
    confirm = input("Are you sure you want to delete instance '{}' (yes/no)? ".format(instances[selected_instance]["label"]))
    
    # Delete the selected instance if the user confirms
    if confirm.lower() == "yes":
        response = requests.delete(delete_instance_endpoint.format(instance_id), headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Instance successfully deleted.")
        else:
            print("Failed to delete instance. Error: {}".format(response.text))
    else:
        print("Deletion cancelled.")
else:
    print("Failed to get a list of instances. Error: {}".format(response.text))
