import pyspark
from pyspark.shell import spark

textFile = spark.read.text("README.md")

print(textFile.count())