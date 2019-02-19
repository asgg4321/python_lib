# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 15:40
# @File      : interpolation_search.py
"""
本算法类似于
"""
items = [2, 3, 5, 7, 9, 11, 13, 17]

def interpSearch(lst, x):  # 默认lst为均匀有序排布
    low = 0  # 默认为最小值下标
    high = len(lst) - 1  # 默认定义为最大值下标

    while lst[low] < x < lst[high]:
        mid = low +
