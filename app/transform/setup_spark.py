from pyspark.sql import SparkSession

def initialize_spark(app_name):
    """Initialize Spark session."""
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark