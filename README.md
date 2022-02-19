# Spark Mini Project
## Automobile post-sales report

<img width="600" alt="Screen Shot 2022-02-18 at 8 11 09 PM" src="https://user-images.githubusercontent.com/70767722/154779887-6610640a-577c-4d17-80fc-ab1d465224e9.png">

NOTE: This mini project is the continuation of the [Hadoop mini project](https://github.com/Andy-Pham-72/hadoop-mini-project).

Consider an automobile tracking platform that keeps track of history of incidents after a new vehicle is sold by the dealer. Such incidents include further private sales, repairs and accident reports. This provides a good reference for second hand buyers to understand the vehicles they are interested in.

The same dataset of a history report of various vehicles is provided. Your goal is to write a Spark job to produce a report of the total number of accidents per make and year of the car.

## Objectives

With this mini project, you will exercise using Spark transformations to solve traditional MapReduce data problems. It demonstrates Spark having a significant advantage against Hadoop MapReduce framework, in both code simplicity and its in-memory processing performance, which best suit for the chain of MapReduce use cases.

# Step 1
From you **Local Terminal** run [upload_spark_files.sh](https://github.com/Andy-Pham-72/spark-mini-project/blob/master/upload_spark_files.sh) to upload to the root directory in the VirtualBox:
![Screen Shot 2022-02-18 at 8 03 30 PM](https://user-images.githubusercontent.com/70767722/154779910-00bd1418-90c6-49f6-9384-3f8cb90d13d5.png)


# Step 2:
From the SandBox's Web Shell Client, run command:
```bash
$ spark-submit AutoSaleExtractSpark.py
```

# Step 4:
Double check the **final_output.txt** file in the SandBox's Web Shell Client:
```bash
$ cat final_output.txt
```
![Screen Shot 2022-02-18 at 8 08 50 PM](https://user-images.githubusercontent.com/70767722/154779913-47961896-27df-4177-b0aa-04dfbfd0c8b9.png)

# Step 5:
Download **final_output.txt** file from SandBox's Web Shell Client's root directory. From local Terminal, run below command:
```bash
$ scp -P 2222 root@127.0.0.1:/root/final_output.txt [local directory]
```


Reference:
- Difference between `groupByKey()` and `reduceByKey()` in Spark [Link](https://www.hadoopinrealworld.com/what-is-the-difference-between-groupbykey-and-reducebykey-in-spark/)