import os, time, sys, shutil
import concurrent.futures

#gives best result with 2 threads
mThreads = 13

#take command line arguments if any
#set mThreads equal to the first argument
if(len(sys.argv)==2):
    mThreads = int(sys.argv[1])

#name of the directory from where we want to fetch files
inputDir = 'InputFiles'
#name of the directory where we want to store processed file
outputDir = 'OutputFiles'

#create a new directory
#if it already exists then delete it and create a new one
try:
    shutil.rmtree(outputDir)
    os.mkdir(outputDir)
except:
    os.mkdir(outputDir)


#function to convert contents of file to upper case
def upperFile(fileNo):

    inputFile = os.path.join( os.getcwd(), inputDir, 'file{}'.format(str(fileNo)))
    
    #given file will open in read mode
    fin = open(inputFile,'r')
    #fetch the data of file convert all the words to uppercase ans store it all as string
    upper_string = fin.read().upper()
    fin.close()
    
    processedFile = os.path.join(os.getcwd(),outputDir,'file{}'.format(str(fileNo)))
    #given file will open in write mode
    fout = open(processedFile,'w')
    #write the converted data into the file
    fout.write(upper_string)
    fout.close()

def upperFileBundle(file1, file2):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as exec:
        for i in range(file1,file2):
            exec.submit(upperFile,i)
        

start = 0
for i in range(1,6):

    wall_clock_start_time = time.perf_counter()

    upperFileBundle(start*100,(start+i)*100)

    start += i

    wall_clock_total_time = time.perf_counter() - wall_clock_start_time
    
    
    print(int(i*100),' ',float(wall_clock_total_time))
