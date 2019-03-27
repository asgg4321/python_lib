# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/3/24 17:03
# @File      : KNN_DEMO.py
"""
最近邻算法实现
"""
import numpy as np


class NearestNeighbor:
    def __init__(self):
        pass

    def train(self, X, y):
        """
        最近邻分类器记住所有的数据参数
        :param X: X 是N x D的数据，每一行都是一份数据
        :param y: y是长度为N的一维数据
        :return:
        """
        self.Xtr = X
        self.ytr = y


    def predict(self, X):
        num_test = X.shpae[0]
        Ypre = np.zeros(num_test, dtype=self.ytr.dtype)

        for i in range(num_test):
            """找到最相近的图像"""
            """使用L1(曼哈顿距离) 距离作为衡量标准"""
            distance = np.sum(np.abs(self.Xtr - X[i,:]),axis=1)
            min_index = np.argmin(distance)
            Ypre[i] = self.ytr[min_index]

        return Ypre


if __name__ == '__main__':
    pass
