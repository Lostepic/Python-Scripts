import requests

proxmox_host = "https://prox.example.com"
proxmox_user = "root@pam"
proxmox_password = "example"

def check_proxmox_api(proxmox_host, proxmox_user, proxmox_password):
    # Set up the request headers with the required authentication
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Build the authentication payload
    data = {
        "username": proxmox_user,
        "password": proxmox_password
    }

    # Send a post request to the Proxmox authentication endpoint
    response = requests.post(f"{proxmox_host}/api2/json/access/ticket", headers=headers, data=data)

    # If the response status code is 200 (OK), the API is working
    if response.status_code == 200:
        print("Proxmox API is working!")
    else:
        print(f"Proxmox API is not working. Response status code: {response.status_code}")

check_proxmox_api(proxmox_host, proxmox_user, proxmox_password)
