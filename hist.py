import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
from matplotlib.ticker import FuncFormatter
import sys
def is_not_exec(val):
    if val >= 0.0005000000 and val <= 0.0007000000 :
        return True
    return False

def to_percent(y,position):
    return str(100*y)+"%"#这里可以用round（）函数设置取几位小数
file_name=sys.argv[1]
data= pd.read_csv(file_name,usecols=['Time'])
#data= pd.read_csv('test500.2',usecols=['Time'])
data['Time'] = data['Time'].astype(float)
#clo_t = float(data['Time'].strip())
clo_t = data['Time'].tolist()
clo_t = list(filter(is_not_exec, clo_t))
# must ns to us
max_t = max(clo_t)
min_t = min(clo_t)
mean_t = np.mean(clo_t)
print('max=','%f' % max_t,'min =','%f' % min_t, 'mean =','%f' % mean_t, 'count =','%d' % len(clo_t ))
#clo_t = list(map(lambda x: x*1000, clo_t))
#fig = plt.figure(figsize=(64,16))
fig = plt.figure()
ax = fig.add_subplot()
bins= [min_t, max_t]
#ax.set_ylim(0, 20)

plt.xlabel("Weight")
plt.ylabel("Probability")
ax.set_xlim(bins)
#plt.tick_params(axis='x', labelsize=32)    # 设置x轴标签大小
plt.xticks(rotation=-20)    # 设置x轴标签旋转角度
#fomatter=FuncFormatter(to_percent)
#plt.gca().yaxis.set_major_formatter(fomatter)
count=len(clo_t )
weights = np.ones_like(clo_t)/float(count)
#如果想设置每根柱子的宽度可以使用rwidth的参数
ax.hist(clo_t, bins=5, color='blue',  weights=weights, rwidth=0.5)
plt.savefig("ether.png") 
###################################################################################
#使用ax.hist()函数想要把数据转为密度直方图，但发现直接使用density=true得到的值很奇怪，y轴甚至会大于1，不符合我的预期。
#查了资料发现density=ture的意思是保证该面积的积分为1，并不是概率和为1，因此我们需要对其进行改进。
#最简单对方法就是对每个bin增加权重，强迫它为我们的概率值：
#
#weights = np.ones_like(myarray)/float(len(myarray))
#plt.hist(myarray, weights=weights)
