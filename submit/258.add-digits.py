class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num
        y = 0
        while True:
            while True:
                y += x % 10
                x = x // 10
                if x == 0:
                    break
            if y < 10:
                return y
            x = y
            y = 0
