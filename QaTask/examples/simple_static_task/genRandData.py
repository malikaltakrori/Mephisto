import numpy as np


with open('QaTask/examples/simple_static_task/theData/realData_fullRun.csv') as fin :
    allRows = fin.readlines()
    
    # put per row in a list 
    methods = {}
    for row in allRows[1:]: # skip the header row
        parts = row.replace("\n", "").split('","')
        
        try:
            methods[parts[4]].append(row)
        except:
            methods[parts[4]] = [row]
            
n_sample = 8
with open('QaTask/examples/simple_static_task/theData/realData_5m8q5a.csv', 'w') as fout:
    for method in methods:    
        method_rows = methods[method]
        np.random.shuffle(method_rows)
        for row in method_rows[:n_sample]:
            fout.write(row)
        
        