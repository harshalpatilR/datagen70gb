# Install Boto to the project
#!pip3 install boto

# Create the Boto S3 connection object.
from boto.s3.connection import S3Connection
aws_connection = S3Connection()
        
# Download the dataset to file 'faithful.csv'.
bucket = aws_connection.get_bucket('harshalpatil-s3')
key = bucket.get_key('loans_accepted_2007_to_2018Q4.csv')
key.get_contents_to_filename('/home/cdsw/faithful.csv')