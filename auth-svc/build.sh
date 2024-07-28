#!/bin/bash

docker login
docker build --tag rrverma316/auth:v2 . -f Dockerfile
docker push rrverma316/auth:v2