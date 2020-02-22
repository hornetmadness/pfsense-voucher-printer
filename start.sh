#!/usr/bin/env bash

gunicorn --config config.py --chdir /app wsgi:app --access-logfile=-
