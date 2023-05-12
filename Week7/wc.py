from pyspark import SparkContext
if __name__ == "__main__":
	sc = SparkContext("local", "word count")
	sc.setLogLevel("ERROR")
	lines = sc.textFile("/user/in")
	words = lines.flatMap(lambda line: line.split(" "))
	wc = words.countByValue()
	for word, count in wc.items():
		print("{}:{}".format(word, count))
	sc.stop()
