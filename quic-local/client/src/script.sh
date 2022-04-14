#!/bin/sh

echo "Hello from $HOSTNAME"

curl https://172.17.0.2:443 --http3
