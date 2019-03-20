# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/2/20 15:08
# @File      : counting_sort.py
import sys

items = [4, 5, 3, 2, 7]


#  Time Complexity O(n+k)
#  Space Complexity O(k)
def countingSort(lst):
    items = list(lst)

    min = sys.maxsize
    max = -sys.maxsize
    for x in items:
        if x > max: max = x
        if x < min: min = x

    counts = [0] * (max - min + 1)
    for x in lst:
        counts[x - min] += 1

    total = 0
    for i in range(min, max + 1):
        oldCount = counts[i - min]
        counts[i - min] = total
        total += oldCount

    for x in lst:
        items[counts[x - min]] = x
        counts[x - min] += 1

    return items


sortItems = countingSort(items)

print(items)
print(sortItems)
