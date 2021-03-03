<img src="logo.png" width="200">

## Backend

This repo contains the backend(gunicorn, flask, and darknet model) for ilytics.sg 


## Run Instruction


1. Clone this repository

`git clone https://github.com/dsaidgovsg/ilytics.git`

2. Navigate into the repository

`cd ilytics`

3. Ensure that the 4 files are in ./aimodel folder before running the following steps.

> 1. `.cfg`
> 2. `.data` 
> 3. `.names`
> 4. `.weights`

4. Build the docker image
`docker build . --tag ilytics_backend_cpu`

5. Run the docker container
`docker run -itd -p 8888:8888 ilytics_backend_cpu`

6. Check if container is running
> Run the following command and ensure ilytics_backend_cpu is visible on the "Images" column
- `docker ps`

7. Your Backend is up and running!

