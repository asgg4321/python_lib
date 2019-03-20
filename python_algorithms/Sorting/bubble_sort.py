# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 18:22
# @File      : bubble_sort.py
"""
冒泡排序法，从小到大排列
"""

items = [4,1,5,3,2]
#  Time Complexity O(n^2)
#  Space Complexity O(1)

def bubbleSort(items):
    lst = list(items)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j]<lst[i]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

sortItems = bubbleSort(items)

print(items)
print(sortItems)


#  *** simplified speed test ***
from datetime import datetime

items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()

for i in range(1, count):
    bubbleSort(items)

delta = datetime.now() - start
totalMicroseconds = delta.seconds*1000000 + delta.microseconds

print(totalMicroseconds)