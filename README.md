![alt text](logo.png)

## Backend

This repo contains the backend(gunicorn, flask, and darknet model) for ilytics.sg 

## Deploying new weights and cfg instruction

- Change the S3 directory at `run.sh` file for both `.cfg` and `.weights` 

- Follow the **Run Instruction** below

## Run Instruction
Note: Do not terminate the existing EC2 instance just ssh into the running EC2 instance

- Stop the existing the guicorn process, running the old inference model

- `rm -rf ilytics`

- `git clone https://github.com/dsaidgovsg/ilytics.git`

- `cd ilytics`

- `docker build -t ilytics-backend .`

- `docker container run --rm --runtime=nvidia --publish 8080:8888 ilytics-backend`




