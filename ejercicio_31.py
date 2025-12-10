from pyspark.sql import SparkSession

spark = SparkSession.builder .appName("mi_primer_pyspark") .getOrCreate()

print(spark)
