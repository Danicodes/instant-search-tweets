#!/usr/bin/env python

# Resources:
# https://nealcaren.org/lessons/twint/
# https://github.com/twintproject/
# Pulling favorites is unfortunately broken unless you have the user id
#
#
import os,sys,re
import download_tweets
from db_management import *

# import google.cloud.storage as gcs
#
# client = gcs.Client()
# bucket = client.bucket('my-bucket')
# blobs = list(bucket.list_blobs(prefix='data/'))
#
# my_df.to_csv('tmp.csv')
# local_tmp_path = ('tmp.csv')
# target_blob = bucket.blob('data/file.csv')
# target_blob.upload_from_file(open(local_tmp_path, 'r'))