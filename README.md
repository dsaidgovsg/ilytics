## Backend

This repo contains the backend(flask and darknet model) for ilytics.sg 

## Run Instruction

- `docker build -t ilytics-backend .`

- `docker container run --rm --runtime=nvidia --publish 8080:8888 ilytics-backend`



