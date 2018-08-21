class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        if num == 0:
            return '0'
        elif num < 0:
            num = -num
            sign = '-'
        else:
            sign = ''
        while num > 0:
            s += str(num % 7)
            num = num // 7
        return sign + s[::-1]

