#!/bin/bash

FLASK_PROJ_DIR="${HOME}/workspace/flask_project"
HOST="127.0.0.1"
PORT="5000"
WITH_ENV="true"
LOGGING_LEVEL=2

function cleanup {

    if [ WITH_ENV = "true" ]
    then
        deactivate
        rm -rf $TEST_DIR/venv_hd_proxy_tests
    fi

    echo "Killing Flask Project with pid: ${FLASK_PROJ_PID}"
    kill -2 ${FLASK_PROJ_PID}
}

function show_help {
    echo "=================================================== HELP ================================================="
    echo "|       Flags         |                  Info                  |         Default             | Required? |"
    echo "|-------------------  |----------------------------------------|-----------------------------|-----------|"
    echo "| -f <directory>      | Directory to the Flask project folder  | ~/workspace/flask_project   |     N     |"
    echo "| -u <host as string> | url for the host                       | 127.0.0.1                   |     N     |"
    echo "| -p <port as string> | port                                   | 5000                        |     N     |"
    echo "| -e <bool as string> | create and run virtual environment     | true                        |     N     |"
    echo "| -l <1-6 level>      | logging level 1-6 (DEBUG - FATAL)      | 2 - INFO                    |     N     |"
    echo "=========================================================================================================="
}

while getopts ":f:u:p:e:l:h" OPT; do
    case $OPT in
        f) FLASK_PROJ_DIR=$OPTARG;;
        u) HOST=$OPTARG;;
        p) PORT=$OPTARG;;
        e) WITH_ENV=$OPTARG;;
        l) LOGGING_LEVEL=$OPTARG;;

        h) show_help
            exit 0;;
        ?) echo "$OPTARG is not a valid flag, execute with -h for help"
            exit 0;;
    esac
done

trap cleanup EXIT SIGINT SIGTERM

if [ $WITH_ENV = "true" ]
then
    virtualenv venv_flask_tests
    . venv_flask_tests/bin/activate

    pip install .
fi

nohup python $FLASK_PROJ_DIR/main.py --host $HOST --port $PORT & disown
FLASK_PROJ_PID=$!
echo "Flask Project has pid: ${FLASK_PROJ_PID}"

echo "Waiting for the Flask Project to start."
sleep 3

case $LOGGING_LEVEL in
    1) LEVEL="DEBUG";;
    2) LEVEL="INFO";;
    3) LEVEL="WARNING";;
    4) LEVEL="ERROR";;
    5) LEVEL="CRITICAL";;
    6) LEVEL="FATAL";;

    *) echo "$LOGGING_LEVEL is not a valid logging level, assigning default"
       LEVEL="INFO";;
esac

behave --logging-level=${LEVEL} features/
