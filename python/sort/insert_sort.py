# -*- encoding:utf-8 -*-

import random

data = []

data_len = 100

for x in range(1, data_len + 1):
    data.append(random.randint(1, 100))

def insert_sort(data, start, end):
    index = start + 1
    while index <= end:
        back = index
        while back > start:
            if data[back] < data[back - 1]:
                data[back], data[back - 1] = data[back -1], data[back]
                back -= 1
            else:
                break
        index += 1

print data
insert_sort(data, 0, data_len - 1)
print data
