import numpy as np
import matplotlib.pyplot as plt
from  scipy.stats import pearsonr 
#求相关系数
# 准备数据
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 7, 11])
x = np.array([0.0,2.0,4.0,6.0,8.0,10.0,12.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,48.0,50.0])
y= np.array([69.15,91.09,121.06,142.86,148.21,149.21,149.27,149.24,149.29,148.49,149.08,149.15,147.88,131.59,74.33,56.56])
# y=y[::-1]#转置
colection=np.polyfit(x,y,10)
#系数
func=np.poly1d(colection)
print(func)
# plt.text(5,2.1,func)
#方程
r=pearsonr(x,y)
print(r)
plt.scatter(x,y,label='new bee')
x_values = np.linspace(0, 50, 10000)
# 生成点来拟合，之前的点不管
plt.plot(x_values,func(x_values),'r',label='function')
#连线
plt.grid()
plt.show()


