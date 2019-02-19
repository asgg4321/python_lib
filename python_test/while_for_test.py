# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 13:50
# @File      : while_for_test.py
from datetime import datetime

maxL = 10000000  # 循环的极限
j = 0

start = datetime.now()
for i in range(maxL):
    if i == maxL - 1:
        break
print(datetime.now() - start)

start = datetime.now()
while True:
    if j == maxL - 1:
        break
    j += 1
print(datetime.now() - start)
