#!/bin/bash

# System Update
echo "Updating system..."
pkg update && pkg upgrade -y

# Tools Install karna
echo "Installing Python and Browser..."
pkg install python chromium tur-repo git -y
pkg install chromedriver -y

# Python Libraries
echo "Installing Python Libraries..."
pip install selenium

# mmail tool ko download karna
echo "Cloning mmail toolkit..."
if [ -d "mmail" ]; then
    echo "mmail already exists, skipping clone."
else
    git clone https://github.com/mao2116/mmail.git
fi

echo "--- SETUP COMPLETE ---"
