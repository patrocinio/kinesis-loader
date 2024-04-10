import json
import time
import urllib.request
import json
import os

def lambda_handler(event, context):

    # Run for 5 minutes
    for iter in range(1, 5*60):
        print("Sending")
        time.sleep(1)
    