# -*-coding:utf-8-*-
# Author: alphadl
# 001两数之和.py 2018/8/7 09:18

"""
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

#暴力解法复杂度O(n^2)
class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rst = []
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    rst.append(' '.join(sorted([str(i), str(j)])))
        return map(int, sorted(set(rst))[0].split())


# test
# nums, target = [2, 7, 11, 15], 9
nums, target = [3, 2, 4], 6
ss = Solution(nums, target)

print ss.twoSum()
