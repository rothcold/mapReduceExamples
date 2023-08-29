#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from pyspark.sql.functions import split, avg
from pyspark.sql import Window
from pyspark.sql.functions import window, window_time


spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()  # type: ignore
spark.sparkContext.setLogLevel("ERROR")

# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = (
    spark.readStream.format("socket")
    .option("host", "127.0.0.1")
    .option("port", 9999)
    .load()
)
indicators = lines.select(
    split("value", ":")[0].alias("indicator"),
    split("value", ":")[1].cast("FLOAT").alias("value"),
    current_timestamp().alias("time"),
)


w = indicators.groupBy("indicator", window("time", "60 seconds")).agg(
    avg("value").alias("avg")
)
avarage = w.select(
    w.window.start.cast("string").alias("start"),
    w.window.end.cast("string").alias("end"),
    "indicator",
    "avg",
)
# avarage = indicators.withColumn("avg", avg("value").over(w))

# Start running the query that prints the running counts to the console
query = avarage.writeStream.outputMode("complete").format("console").start()
# query = avarage.writeStream.format("console").start()

query.awaitTermination()
