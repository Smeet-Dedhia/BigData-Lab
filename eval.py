from pyspark import SparkContext
from functools import partial
import math

if __name__ == "__main__":
	sc = SparkContext("local","myProgram")
	sc.setLogLevel("ERROR")
	
	def Sqrt(x):
		if x>=0:
			return math.sqrt(x)
		
	myList = [4,9,0,-4]
	
	rdd = sc.parallelize(myList)
	
	rdd2 = rdd.map(lambda x: Sqrt(int(x)))
	
	for i in rdd2.collect():
		print(i)
	
	sc.stop()
