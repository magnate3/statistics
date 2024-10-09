# python3

```
 curl "https://bootstrap.pypa.io/pip/3.6/get-pip.py" -o "get-pip.py"
```

```
 yum install python3-devel 
 pip3  install pandas
 python3 get-pip.py 
 pip3  install matplotlib
```

# statistics


```
python3 scatter_2ms.py    test2.csv
python3 max_min_2ms.py    test2.csv
```

+ 适配2ms、1ms、500us需要更改的参数   

```
a1.set_yticks(np.linspace(min_t, max_t, 20)) 
a1.set_yticks(np.linspace(min_t, max_t)) 
```

```
y_major_locator=MultipleLocator(0.01)
```

```
plt.axhline(y=0.6, color="red", linestyle="--")
plt.axhline(y=0.5, color="red", linestyle="--")
plt.axhline(y=0.4, color="red", linestyle="--")
```

+ 可以更改的参数   
```

plt.axhline(y=1.0, color="red", linestyle="--")
plt.axhline(y=1.1, color="red", linestyle="--")
plt.axhline(y=0.9, color="red", linestyle="--")
```

# 折线图

不设置x坐标的尺度，***要求样本> 1百万***，自己会对齐刻度（1百万）  

```
polyline_2ms_max7.py opt13.csv 
python3 polyline_2ms.py opt13.csv 
```

polyline_2ms.py的y轴在(1.75, 2.25)  
polyline_2ms_max7.py的y轴在ylim(min_t, max_t)  

***推荐用polyline_2ms.py，polyline_2ms.py最大样本是1300000***  

![image](pic/poly.png)

# 直方图

```
python3  hist2ms_max7.py  opt13.csv 
```
hist2ms_max7.py 的横坐标在bins= [1.8, 2.8]之间

![image](pic/ether.png)

# 过滤

filter.py

过滤数据 并生成csv