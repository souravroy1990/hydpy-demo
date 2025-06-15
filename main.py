import os
from google.cloud import bigquery

# Set these as environment variables in the Cloud Function configuration
BQ_PROJECT = os.environ.get("BQ_PROJECT")
BQ_DATASET = os.environ.get("BQ_DATASET")
BQ_TABLE = os.environ.get("BQ_TABLE")


def gcs_to_bigquery(event, context):
    """
    Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    bucket = file['bucket']
    name = file['name']
    uri = f"gs://{bucket}/{name}"

    print(f"Processing file: {uri}")

    client = bigquery.Client(project=BQ_PROJECT)
    table_id = f"{BQ_PROJECT}.{BQ_DATASET}.{BQ_TABLE}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # skip header row
        autodetect=True,      # or set schema explicitly
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  # append to table
    )

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    print(f"Starting BigQuery job {load_job.job_id}")
    load_job.result()  # Wait for the job to complete
    print("BigQuery job finished.")

    destination_table = client.get_table(table_id)
    print(f"Loaded {destination_table.num_rows} rows to {table_id}")