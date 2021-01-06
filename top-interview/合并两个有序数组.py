"""
2021年1月6日
给定两个有序整数数组，使合并成一个有序数组

方案：
1.合并后排序
2.双指针从前往后，需要额外存储O(m)
3.双指针从后往前，利用0值位O(1)
"""

input1 = [0]
input2 = [1]


# expect output [1,2,2,3,5,6]

def a():
    def merge(nums1, m, nums2, n):
        nums = nums1[:m]
        for v in nums2:
            nums.append(v)
        if m + n < 2:
            nums1[:] = nums[:]
        l = 0
        r = m + n
        while r > l:
            for v in range((l + 1), r):
                if nums[v] < nums[l]:
                    nums[v] ^= nums[l]
                    nums[l] ^= nums[v]
                    nums[v] ^= nums[l]
            l += 1
        nums1[:] = nums[:]

    merge(input1, 0, input2, 1)


a()
print(input1)
