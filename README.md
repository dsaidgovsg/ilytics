<img src="logo.png" width="200">

## Backend

This repo contains the backend(gunicorn, flask, and darknet model) for ilytics.sg 


## Run Instruction


1. Clone this repository & checkout to the correct branch

 - `git clone https://github.com/dsaidgovsg/ilytics.git`

2. Navigate into the repository

 - `cd ilytics`
 - `git fetch -a`
 - `git checkout -t origin/handover_sfa_cpu`

3. Create a folder names **`aimodel`** in the repo. 

4. Ensure that the 4 files are in ./aimodel folder before running the following steps.

> 1. `.cfg`
> 2. `.data` 
> 3. `.names`
> 4. `.weights`

5. Build the docker image
 `docker build . --tag ilytics_backend_cpu`

6. Run the docker container
 `docker run -itd --name ilytics_backend_cpu_container -p 8888:8888 ilytics_backend_cpu`


7. Run the following command and ensure that the output is similar to the output below
```
docker logs ilytics_backend_cpu_container
```
> `Getting weights from S3`  
> `running gunicorn...`  
> `[2021-03-04 03:34:47 +0000] [7] [INFO] Starting gunicorn 20.0.4`  
> `[2021-03-04 03:34:47 +0000] [7] [INFO] Listening at: http://0.0.0.0:8888 (7)`  
> `[2021-03-04 03:34:47 +0000] [7] [INFO] Using worker: sync`  
> `[2021-03-04 03:34:47 +0000] [10] [INFO] Booting worker with pid: 10`  

8. Your Backend is up and running!

