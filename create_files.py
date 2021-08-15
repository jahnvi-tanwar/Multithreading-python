import concurrent.futures 
import os, shutil, time, random, string
import threading;

#name of the directory in which you want to make new file
dirname = os.path.join(os.getcwd(), 'InputFiles')
print(dirname)

#number of files to be created
totalFiles = 1500

#number of bytes in kiloBytes
kB = 1024 #1 kB

#threads active currently
activeThreads = threading.active_count()


#create a new directory
#if it already exists then delete it and create a new one
try:
    shutil.rmtree(dirname)
    os.mkdir(dirname)
except:
    os.mkdir(dirname)


def createFile(fileNum):
    iteration = 9000
    fileName = dirname + '/file{}'.format(fileNum)

    #open the file
    fstream = open(fileName,'w')

    #size should be between 2MB and 5MB
    required_size = random.randrange(2,5) * 1024

    while True:
        #filling characters in file
        for _ in range(iteration):
            str = ' '.join(random.sample(string.ascii_letters,50))
            fstream.write(str + '\n')

        #until the size of file is greater than or equal to the required size
        if int(os.stat(fileName).st_size) / kB > required_size:
            break

#controller code

#timer starts
time_taken = time.perf_counter()

#create 1500 files
for i in range(totalFiles):
    with concurrent.futures.ThreadPoolExecutor() as exec:
        exec.submit(createFile,i)


#timer stops
time_taken = time.perf_counter() - time_taken

#print the time taken for creating all the files
print(float(time_taken))

#time : 1299 sec