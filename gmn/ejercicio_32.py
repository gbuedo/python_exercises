from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("mi_segundo_pyspark")
    .master("local[1]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# --- Código del DataFrame de prueba ---

data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
columns = ["Name", "ID"]

df_spark = spark.createDataFrame(data, columns)

# Llamada a la acción
df_spark.show()

# Cerrar la sesión de Spark
spark.stop()