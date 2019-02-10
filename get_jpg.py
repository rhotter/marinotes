from pdf2image import convert_from_path
from PIL import Image
import boto3
import io
from secret import bucket_name, user, password

# temp_file_path = 'temp/' + file.filename
# file.save(temp_file_path)
# convert_pdf_to_jpeg(temp_file_path, 'static/pdf/Notes/extra/sample-2.jpeg')

def convert_pdf_to_jpeg(file_path, output_path):
    desired_width, desired_height = 1700, 2200

    image = convert_from_path(file_path, last_page=1)[0]
    current_width, current_height = image.size
    current_aspect_ratio = current_width/current_height
    desired_aspect_ratio = desired_width/desired_height

    if current_aspect_ratio > desired_aspect_ratio: # width too big
        temp_width = int(current_width*desired_height/current_height)
        delta = int((temp_width - desired_width)/2)
        image.resize((temp_width, desired_height))
        image.crop((delta, 0, temp_width - delta, desired_height))
    else: # height too big (or equal)
        temp_height = int(current_height*desired_width/current_width)
        delta = int((temp_height - desired_height)/2)
        image.resize((temp_height, desired_width))
        image.crop((0, delta, 0, temp_height - delta))

    buffer = io.BytesIO()

    image.save(buffer, 'JPEG')

    s3_resource = boto3.resource('s3', aws_access_key_id=user, aws_secret_access_key=password)
    my_bucket = s3_resource.Bucket(bucket_name)
    my_bucket.Object(output_path).put(Body=buffer.getvalue(), ContentType='image/jpeg') # can put name of file here
