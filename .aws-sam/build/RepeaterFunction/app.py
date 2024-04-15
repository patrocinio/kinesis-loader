import json
import time
import json
import logging
import boto3
from botocore.exceptions import ClientError
import time

kinesis_client = boto3.client("kinesis")
stream_name = "lowd"
logger = logging.getLogger(__name__)
tps = 10

def put_record(count):
    try:
        for iter in range(1, tps):

            response = kinesis_client.put_record(
                StreamName=stream_name, Data=json.dumps("anything"), PartitionKey=str(count)
            )
        logger.info ("Put %d records %d in stream %s.", tps, count, stream_name)
        print ("Put %d record %d in stream." % (tps, count))
    except ClientError:
        logger.exception("Couldn't put record in stream %s", stream_name)
        raise
    else:
        return response

def lambda_handler(event, context):

    # Run for 5 minutes
    counter = 0
    for iter in range(1, 5*60):
        start_time = time.time()
        put_record(counter)
        time_spent = time.time() - start_time
        print ("Time spent %s." % time_spent)
        if time_spent < 1:
            time.sleep(1 - time_spent)
        counter = counter+1
    