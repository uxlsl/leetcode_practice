# 541. 反转字符串 II
# https://leetcode-cn.com/problems/reverse-string-ii/

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''

        i = 0
        while i < len(s):
            ss = s[i:i+2*k]
            i += 2*k
            result += ss[:k][::-1] + ss[k:]

        return result
