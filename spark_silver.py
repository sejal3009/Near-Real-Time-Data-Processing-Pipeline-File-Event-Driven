from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from delta import configure_spark_with_delta_pip
from pyspark.sql.types import *

builder = (
    SparkSession.builder
    .appName("BronzeLayer")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
)
spark = configure_spark_with_delta_pip(builder).getOrCreate()
bronze_df = (
    spark.readStream
    .format("delta")
    .load("data/bronze")
)

silver_df = (
    bronze_df
    .filter(col("amount") > 0)
    .dropDuplicates(["event_id"])
)

query = (
    silver_df.writeStream
    .format("delta")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "data/checkpoints/silver"
    )
    .trigger(availableNow=True)
    .start("data/silver")
)

query.awaitTermination()