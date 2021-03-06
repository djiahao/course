"""
    实现一个批量梯度下降算法求解线性回归问题模型
    数据准备：创建模拟样本数据集，满足Y=F(X)的线性数据
    模型构建：模型 线性模型 ∑(Y -θ.T*X)
              策略 经验极小化
              算法 批量梯度下降 θ=θ+α* gd
    模型评估：R^2 = 1- RSS/TSS
    测试手写BGD算法与scikit-learn框架里面的最小二乘算法结果
    画图展示线性回归模型，两种算法准确率相近
"""

import math
import numpy as np

def validata(X, Y):
    """效验X和Y的格式是否正确"""
    if len(X) != len(Y):
        raise Exception("参数异常！")
    else:
        n = len(X[0])
        for l in X:
            if len(l) != n:
                raise Exception("参数异常！")
        if len(Y[0]) != 1:
            raise Exception("参数异常！")

def predict(x, theta, intercept):
    """
    算出预测值
    :param x: 一条样本
    :param theta: 参数向量
    :param intercept: 截距
    :return: y的预测结果
    """
    result = 0.0
    # 1、x与θ相乘
    n = len(x)
    for i in range(n):
        result += x[i] * theta[i]
    # 2、加上那个截距
    result += intercept
    # 3、返回结果
    return result

def predict_X(X, theta, intercept=0.0):
    """
    预测Y[]
    :param X: 特征向量二维矩阵
    :param theta: 参数向量
    :param intercept: 截距
    :return: Y
    """
    Y = []
    for x in X:
        Y.append(predict(x, theta, intercept))
    return Y

def fit(X, Y, alpha=0.01, max_iter=100, fit_intercept=True, tol=1e-4):
    """
    进行模型的训练，返回模型参数θ值与截距
    :param X: 输入的特征属性的矩阵 二维矩阵 m*n m表示样本个数 n就是X的维度数目
    :param Y: 输入的目标属性的矩阵 二维矩阵 m*k m表示样本个数 k表示Y值的个数 一般k=1 目前这个阶段就考虑一个Y值就行了
    :param alpha: 学习率 步长 默认0.01
    :param max_iter: 指定的一个最大的迭代次数 默认100
    :param fit_intercept: 是否训练截距 默认True 训练
    :param tol: 线性回归当中的平方和损失函数的误差值如果小于给定的tol值 就结束迭代 退出循环
    :return: （theta，intercept）
    """
    # 1、效验一下输入的X Y数据格式是否正确
    validata(X, Y)
    # 2、开始训练模型 迭代 计算参数
    # 获取行和列 分别记做样本个数m和特征属性个数n
    m,n = np.shape(X)
    # 定义需要训练的参数 并且给定初始值
    theta = [0 for i in range(n)]
    intercept = 0.0
    max_iter = 100 if max_iter <= 0 else max_iter
    # 开始进行迭代 更新参数

    # 定义一个临时的变量
    diff = [0 for i in range(m)]

    for i in range(max_iter):
        # 在当前θ的取值情况下，预测值与实际值直接的差值
        for k in range(m):
            y_true = Y[k][0]
            y_predict = predict(X[k], theta, intercept)
            diff[k] = y_true - y_predict
        # 对θ进行更新
        for j in range(n):
            # 计算梯度值
            gd = 0
            for k in range(m):
                gd += diff[k] * X[k][j]
            theta[j] += alpha * gd
        # 训练截距(相当于求解θ的时候，对应的维度上的x的取值是1）
        if fit_intercept:
            gd = np.sum(diff)
            # gd = 0
            # for k in range(m):
            #     gd += diff[k] * 1
            intercept += alpha * gd
        # 需要判断损失函数是否已经收敛（损失函数的值是否小于我们给定的那个tol）
        # 1、计算损失函数的值
        # 2、判断损失函数的值与我们给定的tol
        sum_j = 0.0
        for k in range(m):
            y_true = Y[k][0]
            y_predict = predict(X[k], theta, intercept)
            j = y_true - y_predict
            sum_j += math.pow(j, 2)
        sum_j /= m

        if sum_j < tol:
            break
    # 3、返回参数
    return (theta, intercept)

def score_X_Y(X, Y, theta, intercept=0.0):
    # 1、先得到Y的预测值
    Y_predict = predict_X(X, theta, intercept)
    return score(Y, Y_predict)

def score(Y, Y_predict):
    """
    计算回归模型的R^2值
    :param Y: 标签向量
    :param Y_predict: 标签向量预测值
    :return: R^2 准确率
    """
    # 1、计算RSS与TSS
    average_Y = np.average(Y)
    m = len(Y)
    rss = 0.0
    tss = 0.0
    for k in range(m):
        rss += math.pow(Y[k] - Y_predict[k], 2)
        tss += math.pow(Y[k] - average_Y, 2)
    # 2、计算R^2的值
    r_2 = 1.0 - 1.0 * rss/tss
    # 3、返回
    return r_2

#测试一下 BGD 与 scikit-learn里面最小二乘 比较
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif']=[u'simHei']
mpl.rcParams['axes.unicode_minus']=False

# 创建模拟数据（样本数据）
np.random.seed(0)
np.set_printoptions(linewidth=1000, suppress=True) # 设置打印选项

N = 10
x = np.linspace(0, 6, N) + np.random.randn(N)
y = 1.8 * x **3 + x**2 -14*x -7 + np.random.randn(N)

x.shape = -1, 1
y.shape = -1, 1
# print(x)
# print(y)

# 在样本的基础上 进行模型的训练（最小二乘 梯度下降的）
lr = LinearRegression(fit_intercept=True)
lr.fit(x, y)
print('scikit-learn模块自带的最小二乘算法实现-----')
s1 = score(y, lr.predict(x))
print('我们自己写的R^2值的计算：%.5f' % s1)
print('框架里面自带的R^2值：%.5f' % lr.score(x, y))
print('参数列表θ:', lr.coef_)
print('截距：', lr.intercept_)

# 自己写的BGD训练
theta, intercept = fit(x, y, alpha=0.01, max_iter=100, fit_intercept=True)
print('BGD梯度下降算法实现-----')
s2 = score(y, predict_X(x, theta, intercept))
print('我们自己写的R^2值的计算：%.5f' % s2)
print('参数列表θ:', theta)
print('截距：', intercept)

# 画图
plt.figure(figsize=(12, 6), facecolor='w')

# 为了画那条直线 需要产生很多模拟数据
x_hat = np.linspace(x.min(), x.max(), num=100)
x_hat.shape = -1, 1
# 框架里面的最小二乘
y_hat1 = lr.predict(x_hat)
# BGD梯度下降
y_hat2 = predict_X(x_hat, theta, intercept)

plt.plot(x, y, 'ro', ms=10, zorder=3)
plt.plot(x_hat, y_hat1, color='g', lw=2, alpha=0.75, label=u'普通最小二乘，准确率$R^2$:%.3f' % s1, zorder=2)
plt.plot(x_hat, y_hat2, color='b', lw=2, alpha=0.75, label=u'BGD梯度下降，准确率$R^2$:%.3f' % s2, zorder=1)
plt.legend(loc='upper left')
plt.grid(True)
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.suptitle(u'普通最小二乘与BGD梯度下降的线性回归模型比较', fontsize=22)

plt.show()