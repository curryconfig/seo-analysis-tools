#!/bin/bash

pkill -9 chrome
pkill -9 python3

echo "Starting deployment..."

for i in {1..5}
do
   python3 goblok.py > /dev/null 2>&1 &
   sleep 5
done

echo "Deployment successful. Monitoring active."
wait
