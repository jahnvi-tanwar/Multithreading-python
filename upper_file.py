import os, time, shutil


#name of the directory from where we want to fetch files
inputDir = 'InputFiles'
#name of the directory where we want to store processed file
outputDir = 'OutputFiles'

#create a new directory
#if it already exists then delete it and create a new one
try:
    shutil.rmtree(os.path.join(os.getcwd(),outputDir) )
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
    
    for i in range(file1,file2):
        upperFile(i)

start = 0
for i in range(1,6):

    wall_clock_start_time = time.perf_counter()

    upperFileBundle(start*100,(start+i)*100)

    start += i

    wall_clock_total_time = time.perf_counter() - wall_clock_start_time
    
    
    print(int(i*100),' ',float(wall_clock_total_time))