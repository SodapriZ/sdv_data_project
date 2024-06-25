from pyspark.sql.functions import regexp_extract, col

def extract_columns(df):
    """Extract and transform columns."""
    df = df.withColumn('unity', regexp_extract(col('Title'), r'((kg)|(g))\s', 1)) \
           .withColumn('quantity', regexp_extract(col('Title'), r'(\d+)\s(kg|g)', 1).cast('int')) \
           .withColumn('score_of_review', regexp_extract(col('Reviews'), r'Rating:\s(\d+)', 1).cast('int')) \
           .withColumn('number_of_review', regexp_extract(col('Reviews'), r'\(\((\d+)\)\sreviews\)', 1).cast('int')) \
           .withColumn('price_float', (regexp_extract(col('Price'), r'(\d+)€(\d+)', 1).cast('float') +
                                       regexp_extract(col('Price'), r'(\d+)€(\d+)', 2).cast('float') / 100)) \
           .withColumn('coffee_type', regexp_extract(col('Title'), r'(grain|moulu)', 1)) \
           .withColumn('torrefaction_level', regexp_extract(col('Commerce Details'), r'(\d),', 1).cast('int')) \
           .withColumn('brand', regexp_extract(col('Title'), r'[- ]([Cc]afé.*)-.(.*)', 2)) \
           .withColumn('product_name', regexp_extract(col('Title'), r'[- ]([Cc]afé.*(grain |moulu ))(.*)[-]', 3))
    return df