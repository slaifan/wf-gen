#!/bin/bash

# bash capture.sh chrome 5 quic
# bash capture.sh firefox 5 quic
# bash capture.sh edge 5 quic

# bash capture.sh chrome 5 tcp
bash capture.sh firefox 5 tcp
bash capture.sh edge 5 tcp

python3 traffic-analysis.py