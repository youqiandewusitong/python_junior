import pandas as pd
#字典
# dict1={'account':[100,200,300],'owner':['吴思彤','宁晓坤','付爽']}#不能写中文
# dict1={'account':[100,200,300],'owner':[1,2,3]}
# dict1=pd.DataFrame(dict1)
# print(dict1)

#列表 #没有序号要自己加上
# list1=['wu','xiao','wang']
# list2=[1,2,3]
# list=pd.DataFrame(list1,list2)
# print(list)


# zip函数的打包作用,创建字典


###这是因为dict是Python的内置函数，用于创建字典对象。如果在前面声明了一个名为dict的变量，那么这个变量将会覆盖内置函数dict，
# 导致无法正常使用dict函数。因此，为了避免命名冲突，最好不要使用内置函数的名称作为变量名。
# list1=['zhang','zhuang','chen']
# list2=[1,2,3]
# dic=dict(zip(list1,list2))
# dic2=pd.DataFrame(dic)
# print(dic2)
import pandas as pd
from colorama import Fore
list1 = ['zhang', 'zhuang', 'chen']
list2 = [1, 2, 3]
dic = dict(zip(list1, list2))
print(dic)
# 创建 DataFrame，并转置
dic2 = pd.DataFrame(dic, index=[0]).T
print(dic2)
from colorama import Fore
string = 'new bee'
print(f'{Fore.WHITE}string')