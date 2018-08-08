# -*-coding:utf-8-*-
# Author: alphadl
# 007反转整数.py 2018/8/8 11:33

"""

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.raw_reverse(x) if \
            2147483648 > self.raw_reverse(x) > -2147483648 \
            and 2147483648 > x > -2147483648 else 0


    def raw_reverse(self,x):

        return int(str(x)[::-1]) if str(x)[0] != "-" else -int(str(x)[1:][::-1])

# test
ss=Solution()
print ss.reverse(-123)
print ss.reverse(123)
print ss.reverse(120)
print ss.reverse(1534236469)