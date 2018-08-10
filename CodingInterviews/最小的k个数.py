#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 20:38
# @Author  : Qasim
# @File    : 最小的k个数.py
# @Software: PyCharm Community Edition

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        if k > len(tinput):
            return []
        t = sorted(tinput)
        return t[:k]
    import heapq
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        return heapq.nsmallest(k, tinput)

tinput = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 4))
