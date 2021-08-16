# Multithreading-python

Create files, process them and then store the output in new files. Complete the task faster with multithreading in python.

# Task Performed

- For this experiment blocks of 100, 200, 300, 400 and 500 files were given as input.
- upper_file() function defined in upper_file.py and multithreading_upper_file.py was used to convert each alphabet in the file from lower case to upper case. 
- In upper_file.py program task was formed sequentially but in multithreading_upper_file.py the same task was performed with multithreading. To create threads ThreadPoolExecutor (from concurrent.futures module) was used. 
- In main.py program task is performed multiple times varying number of threads each time. This is done to find the optimal number of threads which will perform the task in less time.
- plot_threads.py file is used to plot number of thread vs time graph which is result of main.py program (reportBundle/report_bundle).
- plot_graph.py file is used to plot  number of files vs time double line graph comparing the result of task performed with multithreading and without multithreading.



