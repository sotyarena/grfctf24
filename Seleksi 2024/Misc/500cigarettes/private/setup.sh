#!/bin/bash

if sudo docker build -t 500cigarettes .; then
	echo "Docker image built successfuly"
else
	echo "Failed to build Docker image." >&2
	exit 1
fi

if sudo docker run -dp 0.0.0.0:2000:2000 500cigarettes; then
	echo "Docker container is running at port 2000"
else
	echo "Failed to start Docker container" >&2
	exit 1
fi
