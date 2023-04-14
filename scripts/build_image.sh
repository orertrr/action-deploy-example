#!/bin/sh

set -e

sudo docker build -t test .
sudo docker compose build --no-cahce