# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/19 13:39
# @File      : if_elif_test.py

limit = 10000000

from datetime import datetime

start = datetime.now()
for i in range(limit):
    if i > limit:
        pass
    elif i < limit:
        pass
print(datetime.now() - start)

start = datetime.now()
for j in range(limit):
    if j > limit:
        pass
    if j < limit:
        pass
print(datetime.now() - start)
