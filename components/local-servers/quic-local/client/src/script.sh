#!/bin/bash

echo "Hello from $HOSTNAME"

hostname -I

curl https://172.17.0.2:443 --http3
