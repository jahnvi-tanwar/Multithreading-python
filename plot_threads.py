import matplotlib.pyplot as plt
import numpy as np

data = open('reportBundle/report_bundle','r',encoding='UTF-8')

threads = []
wall_time = []

for line in data:
    inst = [i for i in line.split()]
    threads.append(int(inst[0]))
    wall_time.append(float(inst[1]))
    

plt.title("Wall time")
plt.xlabel('Number of Files')
plt.ylabel('Wall clock Time (sec)')
plt.xticks(np.arange(0, 21, 1)) 
plt.yticks(np.arange(min(wall_time), max(wall_time), 10)) 


plt.title("CPU utilisation")
plt.xlabel('Number of threads')
plt.ylabel('Time (sec)')

plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(min(wall_time), max(wall_time)+10, 10))

plt.plot(threads,wall_time,marker='o',color='g',label='wall_time')

for x,y in zip(threads,wall_time):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,y), textcoords="offset points",xytext=(0,10), ha='center')

plt.legend()
plt.show()

data.close()