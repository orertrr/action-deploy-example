#!/bin/sh

set -e

sudo docker build -t test /app
sudo docker compose build --no-cache
