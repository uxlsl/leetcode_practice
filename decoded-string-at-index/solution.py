class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        s = ''

        for c in S:
            if c.isdigit():
                s *= int(c)
            else:
                s += c
            if K <= len(s):
                break

        return s[K-1]
