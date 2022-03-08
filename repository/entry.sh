#!/bin/sh
echo "Starting gunicorn" && gunicorn -D -b unix:/var/run/gunicorn.sock server:app --preload -w 4 --timeout 20 --graceful-timeout 15 --enable-stdio-inheritance --capture-output 
echo "Starting nginx" && nginx -g 'daemon off;'
