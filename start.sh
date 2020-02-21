#!/usr/bin/env bash

gunicorn -b "0.0.0.0:5000" --chdir /app wsgi:app --access-logfile=-
