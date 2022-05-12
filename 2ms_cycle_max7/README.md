# correct adjust
```
## plt.xticks([])
plt.xticks([])  #不显示x轴刻度值
```

##  y_major_locator
```
y_major_locator=MultipleLocator(0.5)
##把y轴的主刻度interval设置为0.05
```
##  x_major_locator
```
x_major_locator=MultipleLocator(0.05)
```
## error adjust

```
rwidth=0.5  to rwidth=0.1
ax.hist(clo_t, bins=20, color='blue',  weights=weights, rwidth=0.1)
```

```
bins=20  to bins=120
ax.hist(clo_t, bins=120, color='blue',  weights=weights, rwidth=0.1)
```

```
bins= [min_t, 2.4] to bins= [min_t, 8]
ax.set_xlim(bins)
```