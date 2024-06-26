import logging

def write_dataframe_to_mongo(df):
    """Write DataFrame to MongoDB."""
    try:
        df.write.format("mongo").mode("append") \
               .option("database", "sdv_project") \
               .option("collection", "product") \
               .save()
        logging.info("Data written successfully to MongoDB")
    except Exception as e:
        logging.error(f"Error writing data to MongoDB: {e}")
        raise