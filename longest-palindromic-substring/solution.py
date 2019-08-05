# leetcode
# https://leetcode-cn.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def pal(s, i,j,r):
            """
            返回回文
            """
            while 0<=i<len(s) and 0<=j<len(s) and s[i] == s[j]:
                r = s[i] + r + s[j]
                i -= 1
                j += 1
            return r

        ret = ''
        for i in range(len(s)):
            s1 = pal(s, i,i+1, '')
            if len(ret) < len(s1):
                ret = s1
            s1 = pal(s, i-1,i+1, s[i])
            if len(ret) < len(s1):
                ret = s1
        return ret
