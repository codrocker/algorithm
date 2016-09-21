# -*- encoding:utf-8 -*-

import random

data = []

data_len = 100

for x in range(1, data_len + 1):
    data.append(random.randint(1, 100))

def shell_sort(data, start, end):
    print end - start

shell_sort(data, 0, data_len - 1)
print data
