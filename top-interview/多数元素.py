"""
2021年1月6日
从数组中找到多数元素(大于n/2的元素)

方案：
1.循环遍历统计
2.排序取n/2
3.随机数取值后判断是否是众数，但随机数最坏时间复杂度为O(∞)
4.摩尔投票，相同投一票，不同减一票，最后剩下的就是众数

总结：摩尔投票，众数清零的步长大于其他数，会留到最后
"""
import collections
import random

input1 = [2, 2, 1]
input2 = [4, 1, 1, 1, 1]


def majority_element(nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)


def majority_element_random(nums):
    majority_count = len(nums) // 2
    while True:
        candidate = random.choice(nums)
        if sum(1 for elem in nums if elem == candidate) > majority_count:
            return candidate


def majority_element_moore(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


def a():
    print(majority_element(input1))
    print(majority_element(input2))


def b():
    input1.sort()
    input2.sort()
    print(input1[len(input1) // 2])
    print(input2[len(input2) // 2])


def c():
    print(majority_element_random(input1))
    print(majority_element_random(input2))


def d():
    print(majority_element_moore(input1))
    print(majority_element_moore(input2))


a()
b()
c()
d()
