from pyspark.sql import SparkSession

def initialize_spark(app_name):
    """Initialize Spark session."""
    spark = SparkSession.builder.appName(app_name) \
        .config("spark.mongodb.input.uri", "mongodb://localhost:27017") \
        .config("spark.mongodb.output.uri", "mongodb://localhost:27017") \
        .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
        .getOrCreate()
    return spark