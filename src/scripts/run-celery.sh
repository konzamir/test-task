#!/usr/bin/env bash
PROCESS_COUNT=$1;

if [ -z $1 ]; then
  PROCESS_COUNT=1;
fi;

exec python3 -m celery worker -A cache.app -l info -Q task_publish_posts,celery -c $PROCESS_COUNT -B -E;
