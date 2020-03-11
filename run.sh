#!/bin/bash
set -e

echo "Getting weights from S3"
aws s3 cp s3://kelong/weights/yolo-obj_best.weights backup/yolo-obj_best.weights
aws s3 cp s3://kelong/cfg/yolo-obj.cfg yolo-obj-test.cfg

echo "running gunicorn..."
gunicorn --bind 0.0.0.0:8888 wsgi:app
#python3 app.py
