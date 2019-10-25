from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark1 = SparkSession.builder.appName("TextToHive").config("spark.some.config.option", "some-value").getOrCreate()
sc = spark1.sparkContext

# muti delit
lines = sc.textFile("/user/spark/tjtest4")
parts = lines.map(lambda l: l.split("|!"))
centercode = parts.map(lambda p: Row(data01=p[0], data02=p[1]))
centercode_temp = spark1.createDataFrame(centercode)
centercode_temp.show()
centercode_temp.createOrReplaceTempView("tjtest4")
spark1.sql("select * from tjtest4")

# # single delit
# sc = SparkContext()
# spark = SQLContext(sc)
# dfcsv = spark.read.csv(path='/user/spark/tjtest3', header=True, sep='|')
# dfcsv.createGlobalTempView("tjtmptxt")
# dfcsv.show()
# spark.sql("select * from tjtmptxt")
# spark.sql("insert into hive_test.tjtmp as select * from tjtmptxt")
