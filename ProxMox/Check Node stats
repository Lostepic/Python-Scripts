# When using this script and prompted for the hostname it will automatically assume you are using port 8806, if you use just a domain
# for example https:prox.example.com the enter the domain as prox.example.com:443 (if using ssl) or prox.example.com:80
# if you do not have a valid ssl please add the flag 'verify_ssl=False' on line 22 as follows
# proxmox = proxmoxer.ProxmoxAPI(hostname, user=username, password=password, verify_ssl=False)

import proxmoxer
import getpass
import math

def convert_bytes_to_gb(bytes):
    return round(bytes / (1024**3), 2)

def convert_bytes_to_mb(bytes):
    return round(bytes / (1024**2), 2)

# Prompt for Proxmox server login details
hostname = input("Enter Proxmox hostname: ")
username = input("Enter Proxmox username: ")
password = getpass.getpass("Enter Proxmox password: ")

# Connect to the Proxmox server
proxmox = proxmoxer.ProxmoxAPI(hostname, user=username, password=password)

# List nodes and prompt for a selection
nodes = proxmox.nodes.get()
for i, node in enumerate(nodes):
    print(f"{i}: {node['node']}")

selected_node = nodes[int(input("Enter the number of the node you want to check: "))]['node']

# Get the selected node's status
node_status = proxmox.nodes(selected_node).status.get()

# Calculate the amount of RAM in GB
total_ram = convert_bytes_to_gb(node_status['memory']['total'])

# Calculate the uptime in days and minutes
uptime_in_seconds = node_status['uptime']
uptime_in_minutes, _ = divmod(uptime_in_seconds, 60)
uptime_in_days, uptime_in_hours = divmod(uptime_in_minutes, 60)

# Calculate the current CPU usage in percent to 2 decimal points
cpu_usage = node_status['cpu']
formatted_cpu_usage = "{:.2f}".format(cpu_usage)

# Calculate the current RAM usage in GB/MB and free RAM in GB/MB
used_ram = convert_bytes_to_gb(node_status['memory']['used'])
free_ram = convert_bytes_to_gb(node_status['memory']['free'])
used_ram_mb = convert_bytes_to_mb(node_status['memory']['used'])
free_ram_mb = convert_bytes_to_mb(node_status['memory']['free'])

# Print the node status information
print(f"Node: {selected_node}")
print(f"CPU cores: {node_status['cpuinfo']['cores']}")
print(f"CPU model: {node_status['cpuinfo']['model']}")
print(f"Total RAM: {total_ram} GB")
print(f"Uptime: {uptime_in_days} days, {uptime_in_hours} hours, {uptime_in_minutes} minutes")
print(f"CPU Usage: {formatted_cpu_usage}%")
print(f"RAM Usage: {used_ram} GB ({used_ram_mb} MB)")
print(f"Free RAM: {free_ram} GB ({free_ram_mb} MB)")
