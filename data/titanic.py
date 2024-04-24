
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
train_data=pd.read_csv('/Users/WST/Desktop/titanic/train.csv')
# print(train_data.head())
test_data=pd.read_csv('/Users/WST/Desktop/titanic/test.csv')
# print(test_data.head())
rate_women=train_data[train_data['Sex']=='female']['Survived'].mean()
# rate_women=train_data.loc['Survived']['female'].mean()
#不能用
#在 Pandas 中，布尔索引会根据条件选择满足条件的行。布尔索引的工作方式是，如果条件为 True，则选择该行，如果条件为 False，则排除该行
#因此，对于 train_data['Sex']=='female' 这个条件，它返回一个布尔 Series，其中值为 True 的位置对应的行会被选择，而值为 False 的位置对应的行会被排除。
rate_men=train_data[train_data['Sex']=='male']['Survived'].mean()
print("% of women who survived:", rate_women)
print("% of men who survived:", rate_men)
y_Survived=train_data['Survived']
# y_Survived_=test_data['Survived']
features=['Pclass','Sex','SibSp','Parch','Age','Fare','Embarked']
# Pclass  SibSp  Parch   Age     Fare  Sex_female  Sex_male  Embarked_C  Embarked_Q  Embarked_S
# 0         3      1      0  22.0   7.2500       False      True       False       False        True
# 1         1      1      0  38.0  71.2833        True     False        True       False       False
# 2         3      0      0  26.0   7.9250        True     False       False       False        True
# 3         1      1      0  35.0  53.1000        True     False       False       False        True
# 4         3      0      0  35.0   8.0500       False      True       False       False        True
# ..      ...    ...    ...   ...      ...         ...       ...         ...         ...         ...
# 886       2      0      0  27.0  13.0000       False      True       False       False        True
# 887       1      0      0  19.0  30.0000        True     False       False       False        True
# 888       3      1      2   NaN  23.4500        True     False       False       False        True
# 889       1      0      0  26.0  30.0000       False      True        True       False       False
# 890       3      0      0  32.0   7.7500       False      True       False        True       False
#年龄不适合作为独热编码，
x_train=pd.get_dummies(train_data[features])
x_test=pd.get_dummies(test_data[features])
print(x_train)
estimator=RandomForestClassifier()
param_dict={'n_estimators':[120,200,300,500,800,1200],'max_depth':[5,8,15,25]}
#传入的时候要加上中括号
estimator=GridSearchCV(estimator,param_grid=param_dict,cv=10)
#好像也可以用grid里面加选择器进行搜索
# 增加 n_estimators 可以增加森林中树的数量，从而增加模型的复杂度，有助于捕捉数据中的更多细节。增加 max_depth 可以增加单棵树的深度，也会增加模型的复杂度，使其更能拟合训练数据，但也可能导致过拟合。
estimator.fit(x_train,y_Survived)
#grid进行搜索过程
#第一个参数就是给我们这个数据的影响因素的数据类型，第二个就是我们需要辨别的标签，标签的数组，两个都是要数组类型的才可以
#下面那一步不能做，因为测试集里面没有存活率
# score=estimator.score(x_test,y_Survived_)
y_predict=estimator.predict(x_test)
Passenger_Survived=pd.DataFrame({'PassengerId':test_data.PassengerId,'Survived':y_predict})
#字典类型
Passenger_Survived.to_csv('submission.csv', index=False)
#index=False就是不加索引
print(Passenger_Survived)