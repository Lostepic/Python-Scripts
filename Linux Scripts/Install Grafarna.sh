#!/bin/bash

# Detect the Linux distribution
distro=$(cat /etc/*-release | grep ^ID= | cut -d= -f2)

# Set the package manager based on the Linux distribution
if [ "$distro" == "ubuntu" ] || [ "$distro" == "debian" ]; then
  package_manager="apt-get"
elif [ "$distro" == "centos" ] || [ "$distro" == "rhel" ]; then
  package_manager="yum"
else
  echo "Error: unsupported Linux distribution"
  exit 1
fi

# Update the package list and upgrade any existing packages
$package_manager update -y
$package_manager upgrade -y

# Install Docker if it's not already installed
if ! command -v docker &>/dev/null; then
  if [ "$distro" == "ubuntu" ] || [ "$distro" == "debian" ]; then
    $package_manager install -y docker.io
  elif [ "$distro" == "centos" ] || [ "$distro" == "rhel" ]; then
    $package_manager install -y docker
  fi
fi

# Start the Docker service
if [ "$distro" == "ubuntu" ] || [ "$distro" == "debian" ]; then
  service docker start
elif [ "$distro" == "centos" ] || [ "$distro" == "rhel" ]; then
  systemctl start docker
fi

# Enable the Docker service to start at boot
if [ "$distro" == "ubuntu" ] || [ "$distro" == "debian" ]; then
  systemctl enable docker
elif [ "$distro" == "centos" ] || [ "$distro" == "rhel" ]; then
  systemctl enable docker
fi

# Pull the latest Grafana Docker image
docker pull grafana/grafana

# Start a Grafana Docker container
docker run -d -p 3000:3000 --name=grafana grafana/grafana

# Get the server's IP address
server_ip=$(hostname -I | awk '{print $1}')

# Output the URL to access Grafana
echo "Grafana is now available at http://$server_ip:3000"
echo "The default username is admin and the password is admin"
