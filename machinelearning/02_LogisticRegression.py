"""
    Scikit-Learn逻辑回归模型实现对乳腺癌数据进行分类
    数据准备：采用公开数据集，数值型数据，二分类标签
    数据处理：异常数据处理；特征提取；数据归一化
    模型构建：模型 二项逻辑斯谛模型 P(Y=0|X)=1/(1+exp(w*x)
              策略 结构风险最小化 交叉验证 L2正则化
              算法 极大似然函数方法 梯度下降法
    模型评估：R^2 = 1- RSS/TSS
    测试scikit-learn逻辑回归算法结果
    画图展示线性回归模型
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import warnings
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model.coordinate_descent import ConvergenceWarning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif']=[u'simHei']
mpl.rcParams['axes.unicode_minus']=False

# 拦截异常
warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

# 数据读取并处理异常数据
path = "breast-cancer-wisconsin.txt"
names = ['id','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape',
        'Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei',
        'Bland Chromatin','Normal Nucleoli','Mitoses','Class']

df = pd.read_csv(path, header=None,names=names)
# 只要有列为空 就进行删除操作
datas = df.replace('?',np.nan).dropna(how='any')
# print(datas.head(5))

# 1、数据提取以及数据分割
## 提取
X = datas[names[1:10]]
Y = datas[names[10]]

## 分割
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,random_state=0)

# 2、数据格式化（归一化）
ss = StandardScaler()
## 训练模型及归一化数据
X_train = ss.fit_transform(X_train)

# 3、模型构建及训练
## penalty：过拟合解决参数过大，L1或者L2
## sovler：参数优化方式
### 当penalty为L1的时候，参数只能是：liblinear（坐标轴下降法）；
### nlbfgs和cg都是关于目标函数的二阶泰勒展开
### 当penalty为L2的时候，参数可以是：lbfgs（拟牛顿法）、newton-cg（牛顿法变种）、seq（minibatch）
# 维度<10000时，lbfgs法比较好， 维度>10000时， cg法比较好，显卡计算的时候，lbfgs和cg都比seq块
## multi class：分类方式参数：参数可选：ovr（默认）、multinomial；这两种方式在二元分类问题中，效果是一样的；在多元分类问题中，效果不一样
### ovr:one-vs-rest,对于多元分类的问题，先将其看作二元分类，分类完成后，再迭代堆其中一类继续进行二元分类 里面会有多个模型
###multinomial:many-vs-many(MVM),即Softmax分类效果 只有一个模型
## class weight: 特征权重参数

### TODO：Logistic回归是一种分类算法，不能应用于回归中（也就是说对于传入模型的y值来讲，不能是float类型，必须是int类型）

lr = LogisticRegressionCV(multi_class='ovr',fit_intercept=True,Cs=np.logspace(-2,2,20),cv=2,penalty='l2',solver='lbfgs',tol=0.01)
re = lr.fit(X_train, Y_train)

# 4、模型效果获取
r = re.score(X_train, Y_train)
print("R^2值（准确率）：", r)
print("稀疏化特征比率：%.2f%%" % (np.mean(lr.coef_.ravel()==0)*100))
print("参数：", re.coef_)
print("截距：", re.intercept_)
# 获取sigmoid函数返回的概率值p 概率模型
print(re.predict_proba(X_test))

# 数据预测
## a.预测数据格式化
X_test = ss.transform(X_test) # 使用模型进行归一化操作
## b.结果数据预测
Y_predict = re.predict(X_test)

## c.图标展示
x_len = range(len(X_test))
plt.figure(figsize=(14,7), facecolor='w')
plt.ylim(0,6)
plt.plot(x_len, Y_test, 'ro', markersize=8, zorder=3, label=u'真实值')
plt.plot(x_len, Y_predict, 'go', markersize = 14, zorder=2, label=u'预测值,$R^2$=%.3f' % re.score(X_train, Y_train))
plt.legend(loc='upper left')
plt.xlabel(u'数据编号', fontsize=18)
plt.ylabel(u'乳腺癌类型', fontsize=18)
plt.title(u'Logistic回归算法对乳腺癌数据进行分类',fontsize=20)

plt.show()


