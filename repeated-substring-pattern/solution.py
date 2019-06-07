# leetcode 459
# https://leetcode-cn.com/problems/repeated-substring-pattern/
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)):
            if s == s[i:] + s[:i]:
                return True

        return False

class Solution:
    def repeatedSubstringPattern(self, s) :
        return s in (s + s)[1: len(s)*2 -1]
