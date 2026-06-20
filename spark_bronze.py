from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
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
schema = StructType([
    StructField("event_id", IntegerType()),
    StructField("user_id", IntegerType()),
    StructField("event_type", StringType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", StringType())
])

df = (
    spark.readStream
    .schema(schema)
    .json("data/raw_events")
)

query = (
    df.writeStream
    .format("delta")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "data/checkpoints/bronze"
    )
    .trigger(once=True)
    .start("data/bronze")
)


query.awaitTermination()