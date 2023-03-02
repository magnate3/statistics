import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.dates as mdates
def is_not_exec(val):
    if val >= 0.00000001 :
        return True
    return False



print("sys.argv[0]---------%s",sys.argv[0])                                    
print("sys.argv[1]---------%s",sys.argv[1])                                   
file_name=sys.argv[1]
#num = pd.read_csv(file_name,usecols=['No.'])
#num['No.'] = num['No.'].astype(int)
#num_t = num['No.'].tolist()
data= pd.read_csv(file_name,usecols=['Time'])
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
print('big =', '%d' %big , 'big percent', ' %f' %(big/len(clo_t)) )
#a1 = plt.subplot(311)
fig = plt.figure()
a1 = fig.add_subplot()
a1.set_yticks(np.linspace(min_t, max_t, 100)) 
a1.set_yticks(np.linspace(min_t, max_t)) 
y_major_locator=MultipleLocator(0.05)
##把y轴的主刻度interval设置为0.05
a1.yaxis.set_major_locator(y_major_locator)
xMajorLocator = MultipleLocator(10)  # 将x主刻度标签设置为20的倍数
##xMajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式 一位小数的浮点数
#xMinorLocator = MultipleLocator(10)  # 将x轴次刻度标签设置为5的倍数
#a1.xaxis.set_major_locator(xMajorLocator)
#locator = mdates.MinuteLocator(byminute=[0,30])
#locator.MAXTICKS = 1500
#a1.xaxis.set_major_locator(locator)
#a1.xaxis.set_minor_locator(xMinorLocator)
#plt.xlim(0,100)
#ax = plt.axes()
plt.xticks([])  #不显示x轴刻度值
num = [i for i in range(len(clo_t))]
#a1.plot(num,clo_t)

plt.axhline(y=2.0, color="red", linestyle="--")
plt.axhline(y=1.8, color="red", linestyle="--")
plt.axhline(y=2.2, color="red", linestyle="--")
a1.scatter(num,clo_t,s=1)
plt.savefig("./scatter.png", dpi=200)
#print('max=','%f' % clo_t[0],'min =','%f' % clo_t[1])
