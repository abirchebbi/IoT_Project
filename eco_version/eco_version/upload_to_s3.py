#!/usr/bin/env python3
import boto3
import requests
from dotenv import Dotenv

OBJECT_NAME_TO_UPLOAD = 'test_cam.jpg'

def upload_to_s3(filename):
	config = Dotenv('.env')

	S3_NAME = config['BUCKET']
	AWS_ACCESS_KEY = config['ACCESS']
	AWS_SECRET = config['SECRET']

	s3_client = boto3.client(
	    's3',
	    aws_access_key_id = AWS_ACCESS_KEY,
	    aws_secret_access_key = AWS_SECRET
	)

	#Generate the presigned URL
	response = s3_client.generate_presigned_post(
	    Bucket = S3_NAME,
	    Key = filename,
	    ExpiresIn = 10 
	)

	#Upload file to S3 using presigned URL
	files = { 'file': open(filename, 'rb')}
	r = requests.post(response['url'], data=response['fields'], files=files)
	if r.status_code >= 200 and r.status_code < 300:
	    print("success with code: ", r.status_code)
	else:
	    print("error with code: ", r.status_code)
