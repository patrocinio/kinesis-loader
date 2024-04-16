import json
import time
import json
import logging
import boto3
from botocore.exceptions import ClientError
import time
import os

kinesis_client = boto3.client("kinesis")
stream_name = "lowd"
logger = logging.getLogger(__name__)
tps = int(os.environ.get("TPS"))
counter = 0

def put_record():
    try:
        for iter in range(1, tps):
            response = kinesis_client.put_record(
                StreamName=stream_name, Data=json.dumps("anything"), PartitionKey=str(counter)
            )
            counter = counter+1
        logger.info ("Put %d records %d in stream %s.", tps, count, stream_name)
        print ("Put %d record %d in stream." % (tps, counter))
    except ClientError:
        logger.exception("Couldn't put record in stream %s", stream_name)
        raise
    else:
        return response

def lambda_handler(event, context):

    print ("TPS: ", tps)

    # Run for 10 minutes
    for iter in range(1, 10*60):
        start_time = time.time()
        put_record()
        time_spent = time.time() - start_time
        print ("Time spent %s." % time_spent)
        if time_spent < 1:
            time.sleep(1 - time_spent)
    