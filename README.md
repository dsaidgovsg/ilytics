<img src="logo.png" width="200">

## Backend

This repo contains the backend(gunicorn, flask, and darknet model) for ilytics.sg 


## Run Instruction


1. Clone this repository & checkout to the correct branch

 - `git clone https://github.com/dsaidgovsg/ilytics.git`

2. Navigate into the repository

 - `cd ilytics`
 - `git fetch -a`
 - `git checkout -t origin/handover_sfa_gpu`

3. Create a folder name **aimodel**

4. Ensure that the 4 files are in ./aimodel folder before running the following steps.

> 1. `.cfg`
> 2. `.data` 
> 3. `.names`
> 4. `.weights`

5. Build the docker image
 `docker build . --no-cache --tag ilytics_backend_gpu`

6. Run the docker container
 `docker run --gpus=all --name ilytics_backend_gpu_container -itd -p 8888:8888 ilytics_backend_gpu`

7. Check if container is running
```
Run the following command and ensure that the output is similar to the output below
```
- `docker logs ilytics_backend_gpu_container`
> `Getting weights from S3`
> `running gunicorn...`
> `[2021-03-04 03:34:47 +0000] [7] [INFO] Starting gunicorn 20.0.4`
> `[2021-03-04 03:34:47 +0000] [7] [INFO] Listening at: http://0.0.0.0:8888 (7)`
> `[2021-03-04 03:34:47 +0000] [7] [INFO] Using worker: sync`
> `[2021-03-04 03:34:47 +0000] [10] [INFO] Booting worker with pid: 10`

8. Your Backend is up and running!

### Cuda out of memory error
If the gpu memory is not enough for the application, edit `./aimodel/*.cfg` file. Reduce the width and height to a multiple of 64.  
*Do note that reducing the dimensions will affect the accuracy. If accuracy is priority, use `handover_sfa_cpu branch` instead.*
> `Line 8:` ~~`width=832`~~ -> `width=640`  
> `Line 9:` ~~`height=832`~~ -> `height=640` 


