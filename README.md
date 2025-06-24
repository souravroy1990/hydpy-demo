# hydpy-demo
This repository is created for hydpy meetup demo

## Whoever using this repo need to create a service account in gcp, create a gcs bucket and create a .json key file to push the data into GCS bucket.

## Sample .env
BUCKET_NAME=hydpy_demo
DESTINATION_BLOB_PREFIX=data_streamer
SERVICE_JSON=gcp_hydpy_demo.json
CHUNK_SIZE=5
SLEEP_TIME=60
LOG_LEVEL=INFO
