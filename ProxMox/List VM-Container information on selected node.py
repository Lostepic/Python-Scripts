import sys
import subprocess

try:
    import proxmoxer
except ImportError:
    subprocess.run(["pip", "install", "proxmoxer"])
    import proxmoxer

# Prompt the user for the API details
host = input("Enter the hostname or IP address of the Proxmox cluster (if using no port add :443 or :80): ")
user = input("Enter the username for the server: ")
password = input("Enter the password for the server: ")

# Connect to Proxmox cluster
proxmox = proxmoxer.ProxmoxAPI(host=host, user=user, password=password, verify_ssl=True)

# Get a list of nodes
nodes = proxmox.nodes.get()

# Print the list of nodes
for i, node in enumerate(nodes):
    print(f"{i + 1}. {node['node']}")

# Prompt the user to select a node
selected_node = int(input("Select a node (Enter a number): ")) - 1

# Get the containers and virtual machines of the selected node
containers = proxmox.nodes(nodes[selected_node]["node"]).lxc.get()
vms = proxmox.nodes(nodes[selected_node]["node"]).qemu.get()

# Print the containers
print("Containers:")
for container in containers:
    print(f"ID: {container['vmid']}, Name: {container['name']}, Status: {container['status']}")

# Print the virtual machines
print("Virtual Machines:")
for vm in vms:
    print(f"ID: {vm['vmid']}, Name: {vm['name']}, Status: {vm['status']}")
