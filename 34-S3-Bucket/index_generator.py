import boto3
import time

# Initialize S3 client
s3 = boto3.client('s3')

# Function to generate index.html page with counter
def generate_index_page(counter):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Sample Page</title>
    </head>
    <body>
    <h1>Page Counter: {counter}</h1>
    </body>
    </html>
    """
    return html_content

# Function to upload index.html page to S3 bucket
def upload_to_s3(bucket_name, index_content):
    s3.put_object(Bucket=bucket_name, Key='index.html', Body=index_content, ContentType='text/html')

# Main loop to generate and upload index.html every 5 minutes
counter = 0
while True:
    index_content = generate_index_page(counter)
    upload_to_s3('test-bucket-1-eks', index_content)
    counter += 1
    time.sleep(300)  # Sleep for 5 minutes

