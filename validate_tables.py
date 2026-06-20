from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

builder = (
    SparkSession.builder
    .appName("Validation")
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

bronze = spark.read.format("delta").load("data/bronze")
silver = spark.read.format("delta").load("data/silver")

print("\nBRONZE TABLE")
bronze.show()

print("\nSILVER TABLE")
silver.show()

print("Bronze Count:", bronze.count())
print("Silver Count:", silver.count())