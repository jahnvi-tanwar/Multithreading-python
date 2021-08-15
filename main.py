import os;
import matplotlib.pyplot as plt;
import time;
import shutil
import numpy as np

dirname = 'reportBundle'

try:
    shutil.rmtree(dirname)
    os.mkdir(dirname)
except:
    os.mkdir(dirname)

report = open('{}/report_bundle'.format(os.path.join(os.getcwd(),dirname)) ,'w')

threads = []
wall_time = []

for i in range(1,21):
    start = time.perf_counter()

    os.system('python upper_file.py {} > {}/Using_{}_thread'.format(i,dirname,i))

    total = time.perf_counter() - start

    report.write(str(i))
    report.write(' ')
    report.write(str(total))
    report.write('\n')

    wall_time.append(total)
    threads.append(i)
    
report.close()


