from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Read File")
sc = SparkContext.getOrCreate(conf)
text = sc.textFile("/FileStore/tables/sample_txt.txt")
text.collect()
text.dispaly()
df = sc.query("select * from tables/sample_txt")
df.head()
#adding comment 
#adding 2 nd comment 
# addin 3rd comment