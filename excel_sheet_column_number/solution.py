class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {chr(i):i - ord('A') + 1 for i in range(ord('A'), ord('Z')+1)}
        ret = 0
        for num, i in enumerate(reversed(s)):
            ret += m[i] * 26**num
        return ret

