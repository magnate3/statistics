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
#data= pd.read_csv(file_name,usecols=['Time'])
#data= pd.read_csv(file_name,usecols=['Time', 'Protocol'],dtype={'Protocol': str})
data= pd.read_csv(file_name)
data['Protocol']= data['Protocol'].str.strip()
#print(data)
#data=data.query('Protocol == "DHCP"')
#data=data.query('Protocol == "ECAT"')
data=data.query('Time > 0.002')
print(data)
#data = data[data.apply(lambda x: x['Protocol']=='ECAT',  axis=1)]
#data = data.loc[data['Protocol'] =='ECAT']
#data.query('Protocol=="ECAT"')
#data= pd.read_csv('edf.pcap.csv',usecols=['Time'])
data['Time'] = data['Time'].astype(float)
#clo_t = float(data['Time'].strip())
clo_t = data['Time'].tolist()
clo_t = list(filter(is_not_exec, clo_t))
# ns to us
clo_t = list(map(lambda x: x*1000, clo_t))
#print(clo_t)
max_t = max(clo_t)
min_t = min(clo_t)
mean_t = np.mean(clo_t)
print('max=','%f' % max_t,'min =','%f' % min_t)
print('mean =','%f' % mean_t)
big = sum(i >=2.2 for i in clo_t)
small = sum(i <=1.8 for i in clo_t)
print('big =', '%d' %big ,'small =', '%d' %small,'big percent', ' %f' %((big)/len(clo_t)),  'small percent', ' %f' %((small)/len(clo_t)),'total percent', ' %f' %((big+small)/len(clo_t)),  'count =','%d' % len(clo_t ) )
#print('max=','%f' % clo_t[0],'min =','%f' % clo_t[1])
