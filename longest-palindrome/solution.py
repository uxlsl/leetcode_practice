class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = sorted(s)
        count = 0
        index = 0
        length = len(s)
        while index+1 < length:
            if s[index] == s[index+1]:
                count += 2
                index += 2
            else:
                index += 1
        if count == length:
            return count
        else:
            return count + 1
