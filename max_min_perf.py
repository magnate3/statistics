import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
def is_not_exec(val):
    if val >= 0.0005000000 and val <= 0.00070000000 :
        return True
    return False
def is_not_exec_wait(val):
    if val >= 0.4000000 and val <= 0.900000 :
        return True
    return False
def is_not_exec_delay(val):
    if val >= 0.01000 and val <= 0.030000 :
        return True
    return False
def is_not_exec_run(val):
    if val >= 0.0400 and val <= 0.050000 :
        return True
    return False


print("sys.argv[0]---------%s",sys.argv[0])                                    
print("sys.argv[1]---------%s",sys.argv[1])                                   
print("sys.argv[1]---------%s",sys.argv[2])                                   
file_name=sys.argv[1]
clo_name=sys.argv[2]
data=pd.read_csv(file_name,usecols=[clo_name])
data[clo_name] = data[clo_name].astype(float)
clo_t = data[clo_name].tolist()
#print(clo_t)
if 'wait' == clo_name:
    clo_t = list(filter(is_not_exec_wait, clo_t))
elif 'delay' == clo_name:
    clo_t = list(filter(is_not_exec_delay, clo_t))
elif 'run' == clo_name:
    clo_t = list(filter(is_not_exec_run, clo_t))
# ns to us
#clo_t = list(map(lambda x: x*1000, clo_t))
#print(clo_t)
max_t = max(clo_t)
min_t = min(clo_t)
mean_t = np.mean(clo_t)
print('max=','%f' % max_t,'min =','%f' % min_t)
print('mean =','%f' % mean_t)
#print('max=','%f' % clo_t[0],'min =','%f' % clo_t[1])
