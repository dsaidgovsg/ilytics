#!/bin/bash
set -e

echo "Getting weights from S3"
aws s3 cp s3://kelong/weights/yolo-obj_best.weights backup/

echo "running Flask..."
python3 app.py
