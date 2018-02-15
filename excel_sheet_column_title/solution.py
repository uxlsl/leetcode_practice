class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n != 0:
            s += chr(ord('A') + (n-1) % 26)
            n = (n-1) // 26
        return ''.join(reversed(s))
