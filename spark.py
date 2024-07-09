from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Read File")
sc = SparkContext.getOrCreate(conf)
text = sc.textFile("/FileStore/tables/sample_txt.txt")
text.collect()
text.dispaly()