# FROM nvidia/cuda:10.0-cudnn7-devel

# WORKDIR /src

# RUN apt-get update && \
# 		apt-get install -y \
#         python3 \
#         python3-pip \
#         python3-setuptools

# RUN pip3 install setuptools wheel virtualenv awscli --upgrade 
# RUN pip3 install -U scikit-image

# COPY . .

# #ENV LD_LIBRARY_PATH=/usr/local/cuda-10.0/compat/

# RUN pip3 install -r requirements.txt
# RUN chmod +x run.sh

# WORKDIR /src

# EXPOSE 8080

# CMD ["./run.sh"]

FROM nvidia/cuda:10.0-cudnn7-devel AS builder

WORKDIR /src

COPY . .

run  make

FROM nvidia/cuda:10.0-cudnn7-runtime

WORKDIR /src

COPY . .
COPY --from=builder /src/libdarknet.so .

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

RUN apt-get update && \
                apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools &&\
        rm -rf /var/lib/apt/lists/* &&\
        pip3 install setuptools wheel virtualenv awscli --upgrade --no-cache-dir &&\
        pip3 install -U scikit-image --no-cache-dir &&\
        pip3 install -r requirements.txt --no-cache-dir &&\
        chmod +x run.sh

EXPOSE 8080

CMD ["./run.sh"]



