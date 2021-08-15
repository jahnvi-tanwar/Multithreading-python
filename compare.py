import os

outputFolder = 'compare'

try:
    os.mkdir(outputFolder)
except:
    pass

report_multithreading = 'report_multithreading'
report_no_multithreading = 'report_no_multithreading'

os.system('python multithreading_upper_file.py > compare/{}'.format(report_multithreading))
os.system('python upper_file.py > compare/{}'.format(report_no_multithreading))

os.system('python plot_graph.py')