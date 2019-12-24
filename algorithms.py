import random


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        lefthalf = nums[:mid]
        righthalf = nums[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nums[k] = lefthalf[i]
                i = i + 1
            else:
                nums[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            nums[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nums[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return nums


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)


def insertion_sorting(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
