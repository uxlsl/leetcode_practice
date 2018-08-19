class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = '0123456789abcdef'
        if num < 0:
            num = 2**32 + num
        elif num == 0:
            return '0'
        s = ''
        while num > 0:
            s += m[num%16]
            num = num // 16
        return s[::-1]
