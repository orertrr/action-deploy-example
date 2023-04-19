#!/bin/sh

set -e

sudo docker build -t test /app
sudo docker compose --project-directory /app build --no-cache
