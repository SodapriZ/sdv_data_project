import logging

def save_dataframe_to_json(df_cleaned, output_path):
    """Save cleaned DataFrame to JSON."""
    try:
        pandas_df = df_cleaned.toPandas()
        pandas_df.to_json(output_path, orient='records', force_ascii=False, lines=True)
        logging.info(f"Data successfully written to {output_path}")
    except Exception as e:
        logging.error(f"Error saving data to {output_path}: {e}")
        raise