from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("TestSpark").getOrCreate()
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
schema = ["Name", "Age"]
df = spark.createDataFrame(data, schema)
df.show()
