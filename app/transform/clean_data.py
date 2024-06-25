from pyspark.sql.functions import lower, when, col

def clean_data(df):
    """Clean and preprocess data."""
    df_cleaned = df.drop('Price', 'Reviews', 'Commerce Details', 'Title') \
                   .withColumn("unity", lower(col("unity"))) \
                   .withColumn("coffee_type", lower(col("coffee_type"))) \
                   .withColumn("brand", lower(col("brand"))) \
                   .withColumn("product_name", lower(col("product_name"))) \
                   .withColumn("unity", when(col("unity") == "", None).otherwise(col("unity"))) \
                   .withColumn("coffee_type", when(col("coffee_type") == "", None).otherwise(col("coffee_type"))) \
                   .withColumn("brand", when(col("brand") == "", None).otherwise(col("brand"))) \
                   .withColumn("product_name", when(col("product_name") == "", None).otherwise(col("product_name"))) \
                   .dropna()
    return df_cleaned