#!/usr/bin/python
# coding=utf-8

import algorithms
import random
import time
import matplotlib.pyplot as plt

N = [100, 500, 1000, 5000, 10000]
K = 20


def load_random_list(quantity):
    n = list(range(0, quantity))
    random.shuffle(n)
    return n


def mean(func, quantity):
    start_time = time.time()

    for i in range(0, K):
        nums = load_random_list(quantity)
        func(nums)

    end_time = time.time() - start_time

    # print("Время выполнения", end_time, 'sec')
    mean_time = round(end_time / K, 5)
    # print("Среднее время", mean_time, 'sec')
    return mean_time


if __name__ == '__main__':

    quick = []
    merge = []
    insertion = []

    for n in N:
        # print("==== Количество элементов", n)
        # print(">>> Сортировка слиянием")
        merge.append(mean(algorithms.merge_sort, n))

        # print(">>> Быстрая сортировка")
        quick.append(mean(algorithms.quick_sort, n))
        #
        # print(">>> Сортировка вставками")
        # insertion.append(mean(algorithms.insertion_sorting, n))

    plt.plot(N, quick, label='Quick')
    plt.plot(N, merge, label='Merge')
    # plt.plot(N, insertion, label='Insertion')
    plt.legend()
    plt.xlabel('N')
    plt.ylabel('Seconds')
    plt.savefig('plot.png')
