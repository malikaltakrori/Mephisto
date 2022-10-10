import numpy as np

work2do = 'shuffle'

def shuffle_data():
    with open('QaTask/examples/simple_static_task/theData/realData_5m8q5a.csv', 'r') as fin:
        rows = fin.readlines()
        
    with open('QaTask/examples/simple_static_task/theData/realData_5m8q5a.csv', 'w') as fout:
        fout.write(rows.pop(0)) # remove the header row
        np.random.shuffle(rows)
        for row in rows:
            fout.write(row)
    

def gen():
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
    unshuffled = []
    for method in methods:    
        method_rows = methods[method]
        np.random.shuffle(method_rows)
        for row in method_rows[:n_sample]:
            unshuffled.append(row)


    with open('QaTask/examples/simple_static_task/theData/realData_5m8q5a.csv', 'w') as fout:
        np.random.shuffle(unshuffled)
        for row in unshuffled:
            fout.write(row)
    
if __name__ == '__main__':
    if work2do == 'gen':
        gen()
    elif work2do == 'shuffle':
        shuffle_data()
    else:
        raise ValueError('work2do must be "gen" or "shuffle"')
    
