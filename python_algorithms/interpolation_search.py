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
        mid = low + (x - lst[low])*(high-low)//(lst[high] - lst[low])  # 取比较接近于x的值为mid
        if x < lst[mid]:
            high = mid - 1
        elif x > lst[mid]:
            low = mid + 1
        else:
            return mid
    if lst[low] == x:
        return low
    if lst[high] == x:
        return high
    return None

print(interpSearch(items, 1)) # None
print(interpSearch(items, 7))  # 3
print(interpSearch(items, 19))

# *** simplified speed test ***
from datetime import datetime

items = range[0, 1000000]
count = 100


