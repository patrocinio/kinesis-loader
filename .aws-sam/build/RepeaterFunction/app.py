import json
import time
import json
import logging
import boto3
from botocore.exceptions import ClientError

kinesis_client = boto3.client("kinesis")
stream_name = "lowd"
logger = logging.getLogger(__name__)

def put_record(count):
    try:
        response = kinesis_client.put_record(
            StreamName=stream_name, Data=json.dumps("anything"), PartitionKey=str(count)
        )
        logger.info ("Put record %d in stream %s.", count, stream_name)
        print ("Put record %d in stream." % count)
    except ClientError:
        logger.exception("Couldn't put record in stream %s", stream_name)
        raise
    else:
        return response

def lambda_handler(event, context):

    # Run for 5 minutes
    counter = 0
    for iter in range(1, 5*60):
        put_record(counter)
        time.sleep(1)
        counter = counter+1
    