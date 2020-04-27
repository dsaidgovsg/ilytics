#!/bin/bash
set -e

echo "Getting weights from S3"
#If you want to deploy the new weights and cfg, just change the s3 directory only
#Do not change backup/yolo-obj_best.weights and yolo-obj.cfg
aws s3 cp s3://sfarotifer/model/crabbiteV2.0.0/CrabbiteV200-01.weights backup/yolo-obj_best.weights
aws s3 cp s3://sfarotifer/model/crabbiteV2.0.0/CrabbiteV200-01.cfg  yolo-obj.cfg
aws s3 cp s3://sfarotifer/model/crabbiteV2.0.0/CrabbiteV200-01.names  data/obj.names

echo "running gunicorn..."
gunicorn --bind 0.0.0.0:8888 wsgi:app

