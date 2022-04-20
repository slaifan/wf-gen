#!/bin/sh
# ping www.google.com
hostname -I
python3 /src/client-runner.py chrome google.com
