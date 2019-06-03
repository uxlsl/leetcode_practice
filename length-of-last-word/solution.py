class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if words:
            return len(words[-1])
        return 0
