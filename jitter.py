import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
import sys
# https://www.pynote.net/archives/2460
def is_not_exec(val):
    if val >= 0.0005000000 and val <= 0.0007000000 :
        return True
    return False

## RMS jitter

file_name=sys.argv[1]
data= pd.read_csv(file_name,usecols=['Time'])
#data= pd.read_csv('test500.2',usecols=['Time'])
data['Time'] = data['Time'].astype(float)
#clo_t = float(data['Time'].strip())
clo_t = data['Time'].tolist()
clo_t = list(filter(is_not_exec, clo_t))
# ns to us
#clo_t = list(map(lambda x: x*1000, clo_t))
#print(clo_t)
#variance
#https://www.geeksforgeeks.org/python-statistics-variance/
#var_t = np.var(clo_t, ddof=1, dtype=np.float64)
var_t = statistics.variance(clo_t)
print('var=','%f' % var_t)
#std_t = np.std(clo_t, ddof=1)
# Standard deviation of list
std_t = statistics.pstdev(clo_t)
print('std =','%f' % std_t)
