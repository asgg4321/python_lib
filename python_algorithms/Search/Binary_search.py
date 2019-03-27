# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 11:41
# @File      : Binary_search.py
"""
1、常用的二分查找，是在一个有序数组的基础上进行的查找，
2、其实我们可以在数据类型上进行查找，如对于乱序数据，我们可以根据数字的奇偶性
3、也可以从数据的机器码方面进行思考，如数据1000100110，如从数据最后一位，可以筛选一部分，然后依次向前进行筛选
"""

items = [2, 3, 5, 7, 9, 11, 13, 17]  # 定义一个有序数组


def binSearch(lst, x):  # 二分查找算法
    i = 0
    j = len(lst)
    while i != j:
        m = (i + j) // 2
        if x == lst[m]:
            return m
        elif x < lst[m]:
            j = m
        else:
            i = m + 1
    return None


print(binSearch(items, 1))
print(binSearch(items, 7))
print(binSearch(items, 19))

# *******simplified speed test ***
from datetime import datetime

items = range(0, 1000000)
count = 100
start = datetime.now()

for i in range(1, count):
    binSearch(items, 777777)
delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds)
