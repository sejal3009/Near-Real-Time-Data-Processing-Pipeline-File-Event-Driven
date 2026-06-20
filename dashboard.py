import streamlit as st
from pyspark.sql import SparkSession

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

st.title("Streaming Pipeline Dashboard")

df = (
    spark.read
    .format("delta")
    .load("data/silver")
)

pdf = df.toPandas()

st.metric(
    "Total Events",
    len(pdf)
)

st.bar_chart(
    pdf["event_type"].value_counts()
)