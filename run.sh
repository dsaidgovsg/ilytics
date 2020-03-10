#!/bin/bash
set -e

echo "Getting weights from S3"
aws s3 cp s3://kelong/weights/yolo-obj_best.weights backup/

echo "running gunicorn..."
gunicorn --bind 0.0.0.0:8080 wsgi:app
#python3 app.py
