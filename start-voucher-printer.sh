#!/usr/bin/env bash

gunicorn --config config.py --chdir /var/www/vhosts/pfsense-voucher-printer wsgi:app --access-logfile=-
