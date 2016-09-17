# -*- encoding:utf-8 -*-

import random

data = []

data_len = 100

for x in range(1, data_len + 1):
    data.append(random.randint(1, 100))

def bubble(data, start, end):
    while start < end:
        index = start
        while index < end:
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
            index += 1
        end -= 1

print data
bubble(data, 0, data_len - 1)
print data
