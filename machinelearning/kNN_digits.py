'''
   K-近邻算法实现手写数字识别系统
   输入空间：采用UCI公开数据集，被识别数字为32×32像素的黑白图像，经图形处理已转换成文本格式；类别标签为0-9，即10个类别；
   准备数据：将图像转换为测试向量，返回1×1024的Numpy数组；
   分析策略：确定确定欧氏距离度量；k值选择和多数表决分类决策规则；
   测试算法：使用K近邻算法识别手写数字。
'''

import numpy as np
import operator

# def createDataSet():
#     """初始数据集"""
#     group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
#     labels = ['A','A','B','B']
#     return group, labels

def img2vector(filename):
    """将图片转换为测试向量"""
    # 创建向量
    returnVect = np.zeros((1,1024))

    # 打开数据文件，读取每行内容
    fr = open(filename)

    for i in range(32):
        # 读取每一行
        lineStr = fr.readline()

        # 将每行前 32 字符转成 int 存入向量
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])

    return returnVect

# testVector = img2vector('digits/testDigits/0_1.txt')
# print(testVector[0,0:31])

def classify0(inX, dataSet, labels, k):
    """
        KNN算法核心：
        1.确定欧氏距离度量
        2.k值选择为3
        3.采用多数表决分类决策规则
    """
    # 获取样本数据数量
    dataSetSize = dataSet.shape[0]

    # 矩阵运算，计算测试数据与每个样本数据对应数据项的差值
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet

    # sqDistance上一步骤结果平方和
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)

    # 取平方根，得到距离向量
    distance = sqDistance**0.5

    # 按照距离从低到高排序
    sortedDistIndicies = distance.argsort()
    classCount = {}

    # 依次取出最近的样本数据
    for i in range(k):
        # 记录该样本数据所属的类别
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    # 对类别出现的频次进行排序，从高到低
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    # 返回出现频次最高的类别
    return sortedClassCount[0][0]

# group,labels = createDataSet()
# a = classify0([0,0], group, labels, 3)
# print(a)

from os import listdir

def handwritingClassTest():
    """测试算法：使用KNN算法识别手写数字"""
    # 样本数据的类标签列表
    hwLabels = []

    # 样本数据文件列表
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)

    # 初始化样本数据矩阵（M*1024）
    trainingMat = np.zeros((m,1024))

    # 依次读取所有样本数据到数据矩阵
    for i in range(m):
        # 提取文件名中的数字
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)

        # 将样本数据存入矩阵
        trainingMat[i,:] = img2vector('digits/trainingDigits/%s' % fileNameStr)

    # 循环读取测试数据
    testFileList = listdir('digits/testDigits')

    # 初始化错误率
    errorCount = 0.0
    mTest = len(testFileList)

    # 循环测试每个测试数据文件
    for i in range(mTest):
        # 提取文件名中的数字
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])

        # 提取数据向量
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)

        # 对数据文件进行分类
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)

        # 打印KNN算法分类结果和真实的分类
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))

        # 判断KNN算法结果是否准确
        if (classifierResult != classNumStr): errorCount += 1.0

    # 打印错误率
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))

if __name__ == "__main__":
    handwritingClassTest()
