import pandas as pd
import statistics
import csv

df =pd.read_csv("data.csv")
math = df["math score"].tolist()
read = df["reading score"].tolist()
write = df["writing score"].tolist()

math_mean = statistics.mean(math)
read_mean = statistics.mean(read)
write_mean = statistics.mean(write)

print ("The mean for math score is " + str(math_mean))
print ("The mean for reading score is " + str(read_mean))
print ("The mean for writing score is " + str(write_mean))

print ("The median for math score is " + str(statistics.median(math)))
print ("The median for reading score is " + str(statistics.median(read)))
print ("The median for writing score is " + str(statistics.median(write)))

print ("The mode for math score is " + str(statistics.mode(math)))
print ("The mode for reading score is " + str(statistics.mode(read)))
print ("The mode for writiing score is " + str(statistics.mode(write)))

math_std = statistics.stdev(math)
read_std = statistics.stdev(read)
write_std = statistics.stdev(write)

print ("The standard deviation for math score is " + str(math_std))
print ("The standard deviation for reading score is " + str(read_std))
print ("The standard deviation for writing score is " + str(write_std))

math_start,math_end = math_mean-math_std, math_mean+math_std
read_start,read_end = read_mean-read_std, read_mean+read_std
write_start, write_end =write_mean-write_std, write_mean+write_std

print(math_start,math_end)
print(read_start,read_end)
print(write_start, write_end)

count_1=[]
for i in math:
    if(i>=math_start and i<=math_end):
        count_1.append(i)
print("The percentage in math test is "+str(len(count_1)/1000*100))

count_2=[]
for i in read:
    if(i>=read_start and i<=read_end):
        count_2.append(i)
print("The percentage in reading test is "+str(len(count_2)/1000*100))

count_3=[]
for i in write:
    if(i>=write_start and i<=write_end):
        count_3.append(i)
print("The percentage in writing test is "+str(len(count_3)/1000*100))