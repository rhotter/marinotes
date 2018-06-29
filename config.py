import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
