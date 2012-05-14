#! /bin/bash
###
# Startup script for MN Boundary service.
#
#
###

set -e
LOGFILE=/var/log/gunicorn/boundaryservice.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
USER=ubuntu

cd /home/ubuntu/django-projects/mn-boundaryservice
source boundaryservice/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec boundaryservice/bin/gunicorn_django -w $NUM_WORKERS \
    --user=$USER --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE
