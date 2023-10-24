import json
import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
#https://lhf0baevbd.execute-api.us-east-1.amazonaws.com/default/RSAfunctions?ctnum=1

def lambda_handler(event, context):
    ciphertext = int(os.environ["ciphertext"])
    N = int(os.environ["bigN"])
    d = int(os.environ["secret"])
    if not event["queryStringParameters"]:
        return {'statusCode': 200, "body": json.dumps({"N":N, "e":65537, "c":ciphertext})}
    if not ("ctnum" in event["queryStringParameters"]):
        return {'statusCode': 200, "body": json.dumps({"N":N, "e":65537, "c":ciphertext})}
    decryptme=int(event["queryStringParameters"]["ctnum"])
    if (decryptme == ciphertext):
        return {'statusCode': 200, "body": "Sorry can't decrypt that one"}
    plaintext = pow(decryptme, d, N)
    return {
        'statusCode': 200,
        'body': json.dumps({"decrypted": plaintext})
    }
