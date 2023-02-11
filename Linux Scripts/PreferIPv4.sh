#!/bin/bash

# Check if the system is using systemd
if [ -f /etc/systemd/system.conf ]; then
  # Backup the original file
  sudo cp /etc/systemd/system.conf /etc/systemd/system.conf.bak

  # Add the line "DefaultAddressFamily=ipv4" to the file
  sudo sh -c "echo 'DefaultAddressFamily=ipv4' >> /etc/systemd/system.conf"

  # Restart the systemd-networkd service for the changes to take effect
  sudo systemctl restart systemd-networkd

  # Check if the restart was successful
  if [ $? -eq 0 ]; then
    echo "IPv4 preference set successfully using systemd."
  else
    echo "Error setting IPv4 preference using systemd."
  fi
elif [ -f /etc/sysconfig/network ]; then
  # Backup the original file
  sudo cp /etc/sysconfig/network /etc/sysconfig/network.bak

  # Add the line "NETWORKING_IPV6=no" to the file
  sudo sh -c "echo 'NETWORKING_IPV6=no' >> /etc/sysconfig/network"

  # Restart the network service for the changes to take effect
  sudo service network restart

  # Check if the restart was successful
  if [ $? -eq 0 ]; then
    echo "IPv4 preference set successfully using sysconfig."
  else
    echo "Error setting IPv4 preference using sysconfig."
  fi
else
  # The system is using a different network manager, so this script cannot make the changes
  echo "This script does not support your network manager. Please make the changes manually."
fi
