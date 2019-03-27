# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/3/27 20:26
# @File      : data_utils.py
from __future__ import print_function

from six.moves import cPickle as pickle
import numpy as np
import os
from scipy.misc import imread
import platform


def load_pickle(f):
    """
    将二进制字节流序列化为数据对象
    :param f:
    :return:
    """
    version = platform.python_version_tuple()
    if version[0] == '2':
        return pickle.load(f)
    elif version[0] == '3':
        return pickle.load(f, encoding='latin1')
    raise ValueError('invalid python version: {}'.format(version))


def load_CIFAR_batch(filename):
    """
    分批加载CIFAR数据对象
    :param filename:
    :return:
    """
    with open(filename, 'rb') as f:
        datadict = load_pickle(f)
        X=datadict['data']
        Y=datadict['labels']
        X=X.reshape(10000,3,32,32).transpose(0,2,3,1).astype("float")
        y=np.array(Y)
        return X,Y


def load_CIFAR10(ROOT):
    """
    加载所有的cifar数据集
    :param ROOT:
    :return:
    """
    xs=[]
    ys=[]
    for b in range(1,6):
        f = os.path.join(ROOT, 'data_batch_%d' % (b,))
        X,Y = load_CIFAR_batch(f)
        xs.append(X)
        ys.append(Y)
        # 对数组进行拼接，axis=0,为纵向拼接
        Xtr = np.concatenate(xs)
        Ytr = np.concatenate(ys)
        del X,Y
        Xte, Yte = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))
        return Xtr,Ytr,Xte,Yte




def get_CIFAR10_data(num_training=49000, num_validation=1000, num_test=1000,
                     subtract_mean=True):
    """
    从硬盘加载CIFAR-10数据集并为分类做准备。这和我们使用svm的步骤相同，
    但现在提取为单一的函数
    :param num_training:
    :param num_validation:
    :param num_test:
    :param subtract_mean:
    :return:
    """
    cifar10_dir = 'cs231n/datasets/cifar-10-batches-py'
    X_train,y_train,X_test,y_test = load_CIFAR_batch(cifar10_dir)

    # 子采样数据
    mask = list(range(num_training, num_training + num_validation))
    X_val = X_train[mask]
    y_val = y_train[mask]
    mask = list(range(num_training))
    X_train = X_train[mask]
    y_train = y_train[mask]
    mask = list(range(num_test))
    X_test = X_test[mask]
    y_test = y_test[mask]

    # 标准化数据：减去图片的平均值
    if subtract_mean:
        mean_image = np.mean(X_train, axis=0)
        X_train -= mean_image
        X_val -= mean_image
        X_test -= mean_image

    # 翻转令颜色通道排在第一位
    X_train = X_train.transpose(0, 3, 1, 2).copy()
    X_val = X_val.transpose(0, 3, 1, 2).copy()
    X_test = X_test.transpose(0, 3, 1, 2).copy()

    # 将数据打包到文件
    return{
        'X_train':X_train,'y_train':y_train,
        'X_val':X_val,'y_val':y_val,
        'X_test':X_test,'y_test':y_test,
    }

def load_tiny_imagenet(path, dtype=np.float32, subtract_mean=True):
    """

    :param path:
    :param dtype:
    :param subtract_mean:
    :return:
    """