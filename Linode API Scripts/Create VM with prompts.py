import requests
import json

# Prompt for Linode API key
api_key = input("Enter your Linode API key: ")

# Prompt for label
label = input("Enter a label for the new Linode: ")

# Prompt for Linode type
print("Available Linode Types:")
types_response = requests.get("https://api.linode.com/v4/linode/types", headers={
    "Authorization": "Bearer " + api_key
})
types = types_response.json()["data"]
for i, t in enumerate(types):
    print(f"{i + 1}. {t['label']}")
type_choice = int(input("Enter the number corresponding to the desired Linode type: ")) - 1
linode_type = types[type_choice]["id"]

# Prompt for image
print("Available Images:")
images_response = requests.get("https://api.linode.com/v4/images", headers={
    "Authorization": "Bearer " + api_key
})
images = images_response.json()["data"]
for i, image in enumerate(images):
    print(f"{i + 1}. {image['label']}")
image_choice = int(input("Enter the number corresponding to the desired image: ")) - 1
image = images[image_choice]["id"]

# Prompt for region
print("Available Regions:")
regions_response = requests.get("https://api.linode.com/v4/regions", headers={
    "Authorization": "Bearer " + api_key
})
regions = regions_response.json()["data"]
for i, region in enumerate(regions):
    print(f"{i + 1}. {region['label']}")
region_choice = int(input("Enter the number corresponding to the desired region: ")) - 1
region = regions[region_choice]["id"]

# Prompt for password
password = input("Enter a root password for the new Linode: ")

# Create Linode
data = {
    "label": label,
    "type": linode_type,
    "image": image,
    "region": region,
    "root_pass": password
}
response = requests.post("https://api.linode.com/v4/linode/instances", headers={
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}, data=json.dumps(data))

# Print response and IP address
if response.status_code == 200:
    linode_id = response.json()["id"]
    ip_response = requests.get(f"https://api.linode.com/v4/linode/instances/{linode_id}/ips", headers={
        "Authorization": "Bearer " + api_key
    })
    public_ips = ip_response.json()["ipv4"]["public"]
    if public_ips:
        ipv4_address = public_ips[0]["address"]
        print("Linode created successfully!")
        print("Public IPv4 address: {}".format(ipv4_address))
    else:
        print("No public IPv4 address found.")
else:
    error_response = response.json()
    if "errors" in error_response:
        errors = error_response["errors"]
        error_messages = [error["message"] for error in errors]
        print("Linode creation failed with the following errors:")
        for error_message in error_messages:
            print("- {}".format(error_message))
    else:
        print("Linode creation failed with status code {}".format(response.status_code))