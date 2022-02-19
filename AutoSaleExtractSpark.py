from pyspark import SparkContext
from operator import add
from CarSaleETL import extract_vin_key_value, populate_make, extract_make_key_value

# within the sandbox shell run: spark-submit AutoSaleExtractSpark.py

# Initialize SparkContext
sc = SparkContext("local", "My Application")

# Load csv file
raw_rdd = sc.textFile("test_dir/data.csv")

# Use map operation to produce PairRDD
vin_kv = raw_rdd.map(lambda x: extract_vin_key_value(x))

# Populate make and year to all the records
enhance_make = vin_kv.groupByKey().flatMap(lambda kv: populate_make(kv[1]))

# Count the number of occurence for accidents of vehicle make and year
make_kv = enhance_make.map(lambda list_val: extract_make_key_value(list_val))

# Assign final result
final_output = make_kv.reduceByKey(add).collect()
print(final_output)

# Export to text file
with open("final_output.txt", "w") as output:
    for val in final_output:
        print(val)
        output.write(str(val) + "\n")
        
# Stop Spark Application
sc.stop()