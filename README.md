## Backend

This repo contains the backend(flask and darknet model) for ilytics.sg 

## Run Instruction

- `docker build -t iytics-backend .`

- `docker container run --rm --runtime=nvidia --publish 9000:8080 iytics-backend`



