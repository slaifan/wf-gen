#!/bin/bash

export BROWSER="$1"
export REPEAT="$2"
export MODE="$3"

[ -z "$BROWSER" ] && BROWSER=chrome
[ -z "$REPEAT" ] && REPEAT=3
[ -z "$MODE" ] && MODE=quic

DURATION=$(expr 30 '*' $REPEAT + 10)

echo "${BROWSER} browser in ${MODE} mode for $REPEAT times"

function bringup {
    echo "Start the containerised applications..."
    export DATADIR="./data"

    docker-compose --no-ansi --log-level ERROR up -d
}

function teardown {
    echo "Take down the containerised applications and networks..."
    # NB: this removes everything so it is hard to debug from this script
    # TODO: add a `--debug` option instead use `docker-compose stop`.
    docker-compose --no-ansi --log-level ERROR down --remove-orphans -v
    echo "Done."
}

trap '{ echo "Interrupted."; teardown; exit 1; }' INT

while read line
do
    export URL=$line
    echo $URL
    bringup;
    sleep $DURATION
    teardown;
done < websites.csv

