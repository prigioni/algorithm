# -*-coding:utf-8-*-
# Author: alphadl
# 169求众数.py 2018/8/8 11:54

"""
示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data_pool={}
        for i in range(len(nums)):
            tmp_num=nums[i]
            if tmp_num not in data_pool.keys():
                data_pool[tmp_num]=1
            else:
                data_pool[tmp_num]+=1
        return sorted(data_pool.items(), key=lambda d: d[1], reverse=True)[0][0]

#test
ss=Solution()
print ss.majorityElement([3,2,3])
print ss.majorityElement([2,2,1,1,1,2,2])