# Multithreading-python

Create files, process them and then store the output in new files. Complete the task faster with multithreading in python.

# Task Performed

- For this experiment blocks of 100, 200, 300, 400 and 500 files were given as input.
- upper_file() function defined in upper_file.py and multithreading_upper_file.py was used to convert each alphabet in the file from lower case to upper case. 
- In upper_file.py program task was formed sequentially but in multithreading_upper_file.py the same task was performed with multithreading. To create threads ThreadPoolExecutor (from concurrent.futures module) was used. 
- In main.py program task is performed multiple times varying number of threads each time. This is done to find the optimal number of threads which will perform the task in less time.
- plot_threads.py file is used to plot number of thread vs time graph which is result of main.py program (reportBundle/report_bundle).
- plot_graph.py file is used to plot  number of files vs time double line graph comparing the result of task performed with multithreading and without multithreading.

# Observations

Table 1: Comparing execution time of capitalizing file text with multithreading and without multithreading while increasing the number of files by 100 

Number of Files | Time Taken Without Multithreading (s) | Time Taken With Multithreading (s)
--------------- | ---------------------------------|-----------------------------------
100 | 5.928765299999999| 4.4919286
200 | 12.395257399999998 | 9.179343
300  | 18.0341118 |13.407797599999999
400  | 24.9510425 | 18.411698199999996
500  | 31.692379400000007 | 23.569934600000003

Graph 1:

![alt text](https://github.com/jahnvi-tanwar/Multithreading-python/blob/main/compare/compare.png)



