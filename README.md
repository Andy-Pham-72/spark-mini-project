# Spark Mini Project
## Automobile post-sales report

NOTE: This mini project is the continuation of the [Hadoop mini project]().

Consider an automobile tracking platform that keeps track of history of incidents after a new vehicle is sold by the dealer. Such incidents include further private sales, repairs and accident reports. This provides a good reference for second hand buyers to understand the vehicles they are interested in.

The same dataset of a history report of various vehicles is provided. Your goal is to write a Spark job to produce a report of the total number of accidents per make and year of the car.

## Objectives

With this mini project, you will exercise using Spark transformations to solve traditional MapReduce data problems. It demonstrates Spark having a significant advantage against Hadoop MapReduce framework, in both code simplicity and its in-memory processing performance, which best suit for the chain of MapReduce use cases.

# Step 1
From you **Local Terminal** run [upload_spark_files.sh]() to upload to the root directory in the VirtualBox:

# Step 2:
From the SandBox's Web Shell Client, run command:
```bash
$ spark-submit AutoSaleExtractSpark.py
```

# Step 4:
Double check the [final_output.txt] file in the SandBox's Web Shell Client:
```bash
$ cat final_output.txt
```


