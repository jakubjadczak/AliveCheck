#!/bin/bash
set -e

# Sprawdzanie przekazanych argumentów do skryptu
if [ "$1" = 'celery' ]; then
    case "$2" in
        "worker")
            echo "Starting Celery Worker..."
            shift 2
            exec celery -A tasks worker --loglevel=info
            ;;
        "beat")
            echo "Starting Celery Beat..."
            shift 2
            exec celery -A tasks beat --loglevel=info
            ;;
        *)
            echo "Expected 'worker' or 'beat' as arguments"
            exit 1
            ;;
    esac
else
    exec "$@"
fi
