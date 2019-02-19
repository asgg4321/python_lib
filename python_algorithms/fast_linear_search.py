# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 13:48
# @File      : fast_linear_search.py

items = [2, 3, 5, 7, 11, 13, 17]


def linerSearch(lst, x):
    i = 0
    count = len(lst)
    lst.append(x)
    while True:
        if lst[i] == x:
            del lst[count]
            return i if i < count else None
        i += 1


print(linerSearch(items, 1))  # None
print(linerSearch(items, 7))  # 3
print(linerSearch(items, 19))  # None

print(items)

# ***simplifed speed test ***
from datetime import datetime

items = list(range(0, 1000000))
count = 100

start = datetime.now()

for i in range(1, count):
    linerSearch(items, 777777)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(count)

print(totalMicroseconds / count)
