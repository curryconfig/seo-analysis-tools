#!/bin/bash
pkill -9 chrome
pkill -9 python3

echo "=== STARTING DEPLOYMENT ==="

for i in {1..4}
do
   python3 goblok.py &
   sleep 10
done

# Trik Anti-Mokad: Print waktu tiap 60 detik
while true; do
  echo "Pasukan Iblis On Fire: $(date)"
  sleep 60
done
