FROM nvidia/cuda:10.0-cudnn7-devel AS builder

WORKDIR /src

COPY . .

run  make

FROM nvidia/cuda:10.0-cudnn7-runtime

WORKDIR /src

COPY . .
COPY --from=builder /src/libdarknet.so .
COPY ./aimodel/*.weights backup/yolo-obj_best.weights
COPY ./aimodel/*.cfg yolo-obj.cfg
COPY ./aimodel/*.names data/obj.names
COPY ./aimodel/*.data data/obj.data

RUN apt-get update && \
                apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools &&\
	apt install -y libsm6 libxext6 libxrender-dev &&\
        rm -rf /var/lib/apt/lists/* &&\
        pip3 install gunicorn --no-cache-dir &&\
        pip3 install setuptools wheel virtualenv awscli --upgrade --no-cache-dir &&\
        pip3 install -U scikit-image --no-cache-dir &&\
        pip3 install -r requirements.txt --no-cache-dir &&\
        chmod +x run.sh

EXPOSE 8888

CMD ["./run.sh"]




