"""
2021年1月6日
从指定集合中找出只出现一次的数字
方案：
1.遍历集合，利用额外空间存储出现次数或筛选重复，例如hash
2.利用去重集合加法运算和原集合加法运算之差找出元素 *
3.使用亦或找出元素，自身亦或为0且满足交换律和结合律，例如亦或可实现无中间变量交换整型变量

标签：位运算，哈希表
总结：方案大致区别在于空间复杂度O(1)和O(n)，引入额外存储空间也带来了一些操作复杂性
"""

input1 = [2, 2, 1]
input2 = [4, 1, 2, 1, 2]


def a():
    def find_single(i):
        r = 0
        for v in i:
            r = r ^ v
        return r

    print(find_single(input1))
    print(find_single(input2))


def b():
    def find_single(i):
        m = {}
        for v in i:
            if v in m:
                m[v] = m[v] + 1
            else:
                m[v] = 0
        for v in m:
            if m[v] == 0:
                return v

    print(find_single(input1))
    print(find_single(input2))


a()
b()
