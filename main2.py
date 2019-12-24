#!/usr/bin/python
# coding=utf-8

import algorithms
import random
from datetime import datetime
import matplotlib.pyplot as plt

N = [100, 500, 1000, 5000, 10000]
K = 20


def load_random_list(quantity):
    n = list(range(0, quantity))
    random.shuffle(n)
    return n


def mean(func, quantity):
    start_time = datetime.now()

    for i in range(0, K):
        nums = load_random_list(quantity)
        func(nums)

    end_time = datetime.now() - start_time
    mean_time = round(end_time.total_seconds() / K, 5)
    return mean_time


if __name__ == '__main__':

    quick = []
    merge = []
    insertion = []

    for n in N:
        merge.append(mean(algorithms.merge_sort, n))
        quick.append(mean(algorithms.quick_sort, n))
        # insertion.append(mean(algorithms.insertion_sorting, n))

    plt.plot(N, quick, label='Quick')
    plt.plot(N, merge, label='Merge')
    # plt.plot(N, insertion, label='Insertion')
    plt.legend()
    plt.xlabel('N')
    plt.ylabel('Seconds')
    plt.savefig('plot.png')
