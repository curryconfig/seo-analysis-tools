#!/bin/bash

echo "=== INITIALIZING DEPLOYMENT ==="

# Update sistem
sudo apt update -y

# Install Python & Pip jika belum ada
sudo apt install -y python3 python3-pip

# Install Chrome & Chromedriver (Engine utama)
sudo apt install -y chromium-browser chromium-chromedriver

# Install Library Selenium
pip3 install selenium

# Beri ijin eksekusi untuk script gass
chmod +x gass.sh

echo "=== SETUP COMPLETED. READY TO GAS! ==="
