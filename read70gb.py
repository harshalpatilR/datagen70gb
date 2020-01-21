#import boto3
import pandas as pd
import s3fs

df = pd.read_csv('s3://harshalpatil-s3/datagen70gb.csv')
df.head()
df.tail()

