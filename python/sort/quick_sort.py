# -*- encoding:utf-8 -*-

import random

in_data = []

data_len = 40

for x in range(1, data_len + 1):
    in_data.append(random.randint(1, 100))

def quick_sort(data_in, start, end):
    mid = 0
    if start < end:
        mid = partition(data_in, start, end)
        quick_sort(data_in, start, mid -1)
        quick_sort(data_in, mid + 1, end)
def partition(data, start, end):
    index = data[start]

    while (start < end):
        if index <= data[start + 1]:
            data[start + 1],data[end] = data[end],data[start + 1]
            end = end - 1
        else:
            data[start] = data[start + 1]
            start = start + 1
    data[start] = index
    return start

print in_data
quick_sort(in_data, 0, data_len - 1)

print in_data
