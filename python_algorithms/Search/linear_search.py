# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 17:24
# @File      : linear_search.py
"""
线性查询，会对数据从头开始查询，适合于无规律的数据
而之前的二分查找需要数据是有序的，插补法查找都需要数据有序并均匀分布
"""

items=[2, 3, 5, 7, 11, 13, 17]

def linearSearch(lst, x):
    i = 0
    length = len(lst)
    while i < length:
        if lst[i] == x:
            return i
        i += 1
    return None

print(linearSearch(items, 1))
print(linearSearch(items, 7))
print(linearSearch(items, 19))

#  *** simplified speed test ***
from datetime import datetime

items = range(0, 1000000)
count = 100

start = datetime.now()

for i in range(1, count):
    linearSearch(items, 777777)

delta = datetime.now() - start

totalMicroseconds = delta.seconds*1000000 + delta.microseconds

print(totalMicroseconds / count)
