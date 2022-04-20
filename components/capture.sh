#!/bin/bash

DURATION="$1"
export CONCURRENT_THREADS="$2"
export REQUESTS="$3"
export CAPTURETIME=`date +%Y-%m-%d_%H-%M-%S`
REPEAT="$4"


[ -z "$DURATION" ] && DURATION=30
[ -z "$REPEAT" ] && REPEAT=1
[ -z "$CONCURRENT_THREADS" ] && CONCURRENT_THREADS=1
[ -z "$REQUESTS" ] && REQUESTS=20

function bringup {
    echo "Start the containerised applications..."
    export DATADIR="$PWD/data"

    docker-compose --no-ansi --log-level ERROR up -d 
}

function teardown {
    echo "Take down the containerised applications and networks..."
    # NB: this removes everything so it is hard to debug from this script
    # TODO: add a `--debug` option instead use `docker-compose stop`.
    docker-compose --no-ansi --log-level ERROR down --remove-orphans -v
    echo "Done."
}

function add_delays {
    echo "Adding delays to the network..."
    DELAY1=$((RANDOM % 100 + 1))
    DELAY2=$((RANDOM % 100 + 1))
    DELAY3=$((RANDOM % 100 + 1))


    ./container_tc.sh capture-022-nginxssl_nginx_1 $DELAY1
    ./container_tc.sh capture-022-nginxssl_wget_80_1 $DELAY2
    ./container_tc.sh capture-022-nginxssl_wget_443_1 $DELAY3
}

trap '{ echo "Interrupted."; teardown; exit 1; }' INT

for ((i=1; i<=REPEAT; i++))
do
    echo "Repeat Nr " $i
    export REPNUM=$i
    
    bringup;
#    add_delays;
    echo "Capturing data now for $DURATION seconds...."
    sleep $DURATION
    teardown;
done

