# Connect to Spark by creating a Spark session
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()

testdf = spark.read.csv("datagen.csv", header=True, inferSchema=True)