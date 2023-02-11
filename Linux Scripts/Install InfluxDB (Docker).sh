#!/bin/bash

# Check if Docker is installed
if command -v docker > /dev/null; then
    echo "Docker is already installed."
else
    echo "Docker is not installed. Installing Docker."
    # Install Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
fi

# Start the Docker service
sudo service docker start

# Pull the latest InfluxDB image from Docker Hub
sudo docker pull influxdb:latest

# Start a container running InfluxDB in the background
sudo docker run \
    -d \
    -p 8086:8086 \
    -v myInfluxVolume:/var/lib/influxdb \
    influxdb:latest > /dev/null 2>&1

# Get the IP address of the server
IP_ADDRESS=$(ip -4 addr show eth0 | grep -oP "(?<=inet ).*(?=/)")

echo "InfluxDB has been installed and started using Docker."
echo "You can access the InfluxDB UI at http://$IP_ADDRESS:8086."
