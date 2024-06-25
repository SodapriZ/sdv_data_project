import logging

def load_data(spark, file_path):
    """Load JSON data into DataFrame."""
    try:
        df = spark.read.json(file_path, multiLine=True)
        logging.info(f"Data loaded successfully from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        raise