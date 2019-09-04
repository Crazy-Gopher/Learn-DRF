#!/bin/bash
docker stop djangoapp
docker rm djangoapp
docker build -t djangoappimage .
docker run --name djangoapp -d -p 8000:8000 djangoappimage
docker exec -ti djangoapp bash