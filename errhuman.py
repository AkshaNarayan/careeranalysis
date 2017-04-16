import os, sys
from scipy import stats
import numpy as np

for index, line in enumerate(open('lel.csv', 'r').readlines()):
    w = line.split(' ')
    l1 = w[1:33]
    l2 = w[33:33+15]

    try:
        list1 = map(float, l1)
        list2 = map(float, l2)
    except ValueError:
        print ("oh boy")
        break

    result = stats.ttest_ind(list1, list2)
    print result[1]
