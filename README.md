# Multithreading-python

Create files, process them and then store the output in new files. Complete the task faster with multithreading in python.

# Key Concept
Multithreading - Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

# Task Performed

- For this experiment blocks of 100, 200, 300, 400 and 500 files were given as input.
- upper_file() function defined in upper_file.py and multithreading_upper_file.py was used to convert each alphabet in the file from lower case to upper case. 
- In upper_file.py program task was formed sequentially but in multithreading_upper_file.py the same task was performed with multithreading. To create threads ThreadPoolExecutor (from concurrent.futures module) was used. 
- In main.py program task is performed multiple times varying number of threads each time. This is done to find the optimal number of threads which will perform the task in less time.
- plot_threads.py file is used to plot number of thread vs time graph which is result of main.py program (reportBundle/report_bundle).
- plot_graph.py file is used to plot  number of files vs time double line graph comparing the result of task performed with multithreading and without multithreading.

# Observations

Table 1: Comparing execution time of task with varying number of threads

Number of Active Threads | Time Taken (s)
-------------------------|--------------
1 | 178.6066401
2 | 105.1272653
3 | 108.79899689999996
4 | 109.43347
5 | 112.5836483
6 | 110.23512860000005
7 | 108.70159110000009
8 | 108.72304239999994
9 | 108.46342220000008
10 | 107.34687000000008
11 | 107.41258169999992
12 | 105.55386950000002
13 | 105.11554070000011
14 | 105.2745797
15 | 112.48382250000009
16 | 167.87644279999995
17 | 177.6086292
18 | 185.2006136
19 | 184.4623961999996
20 | 183.6998639999997

Graph 1:

![alt text](https://github.com/jahnvi-tanwar/Multithreading-python/blob/main/reportBundle/Figure_1.png)

  Optimal Number of threads = 13

Table 2: Comparing execution time of capitalizing file text with multithreading and without multithreading while increasing the number of files by 100 

Number of threads used = 13

Number of Files | Time Taken Without Multithreading (s) | Time Taken With Multithreading (s)
--------------- | ---------------------------------|-----------------------------------
100 | 5.928765299999999| 4.4919286
200 | 12.395257399999998 | 9.179343
300  | 18.0341118 |13.407797599999999
400  | 24.9510425 | 18.411698199999996
500  | 31.692379400000007 | 23.569934600000003

Graph 2:

![alt text](https://github.com/jahnvi-tanwar/Multithreading-python/blob/main/compare/compare.png)

# Findings:

From graph 2 it is evident that the task performed using multithtreading takes less time. 
Percent decrease in time : 41.01 %



