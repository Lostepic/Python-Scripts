#!/bin/bash

# Determine the OS of the server
if [ -f /etc/redhat-release ]; then
    os="redhat"
elif [ -f /etc/lsb-release ]; then
    os="ubuntu"
elif [ -f /etc/arch-release ]; then
    os="arch"
elif [ -f /etc/gentoo-release ]; then
    os="gentoo"
elif [ -f /etc/SuSE-release ]; then
    os="suse"
elif [ -f /etc/debian_version ]; then
    os="debian"
else
    os="unknown"
    echo "The OS of the server could not be determined."
    exit 1
fi

# Use the correct package manager based on the OS
if [ $os == "redhat" ]; then
    pm="yum"
elif [ $os == "ubuntu" ] || [ $os == "debian" ]; then
    pm="apt-get"
elif [ $os == "arch" ]; then
    pm="pacman"
elif [ $os == "gentoo" ]; then
    pm="emerge"
elif [ $os == "suse" ]; then
    pm="zypper"
else
    pm="unknown"
    echo "The package manager could not be determined."
    exit 1
fi

# Run update and upgrade
$pm update -y
$pm upgrade -y

# Install specified packages
$pm install -y curl wget sudo bpytop iotop nano

echo "Update and upgrade complete. Packages curl, wget, sudo, bpytop, iotop, and nano have been installed."
