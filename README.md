## Synopsis
A generic task queue implementation using the following:
    1) RQ (or Redis Queue - see python-rq.org);
    2) Supervisord (see supervisord.org);
    3) rq-dashboard (see http://github.com/nvie/rq-dashboard)

RQ is used to both submit tasks to a queue which will (in turn) be processed by one of a pool of workers.
The workers are managed by Supervisord.
Rq-dashboard is used to monitor the tasks, workers and queues.

## Installation
In general, any client/calling-code can submit tasks to the task queue provided both are pointed to the same Redis server (IP and port) and database (rd0-15).

To install the requisite modules:
pip install -r requirements.txt

Supervisord:
# to start
    supervisord -c supervisord.conf
# to stop
    kill `cat /private/tmp/supervisord.pid`
# list workers
    ps -ef | grep -i python | grep -i worker | grep -v grep | awk '{print $2}' | xargs


<TBD
        How to install
        How to run
        How to stop
        How to use
>

## Tests
TBD

## License
CC0