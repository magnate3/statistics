import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
def is_not_exec(val):
    if val >= 0.000000001 :
        return True
    return False



print("sys.argv[0]---------%s",sys.argv[0])                                    
print("sys.argv[1]---------%s",sys.argv[1])                                   
file_name=sys.argv[1]
data = pd.read_csv(file_name)
clo_t = data['Time']
clo_t = list(map(lambda x: x*1000, clo_t))
arr = []
for i,val in  enumerate(clo_t):
    if val < 1.90 or val > 2.10 :
         arr.append(i)

data.drop(arr, inplace=True)
data.to_csv("lot3.csv",index=False,encoding="utf-8")
