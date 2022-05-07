#!/bin/bash!

# compose down

docker-compose -f ROS/server-node/docker-compose.yml down && \
docker-compose -f ROS/dev-node/docker-compose.yml down && \

docker-compose -f ROS/server-node/docker-compose.yml up --build -d
docker-compose -f ROS/dev-node/docker-compose.yml up --build -d
