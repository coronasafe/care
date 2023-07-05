#!/bin/bash

watchmedo \
    auto-restart --directory=./ --pattern=*.py --recursive -- \
    celery -A config.celery_app worker -B --loglevel=INFO
