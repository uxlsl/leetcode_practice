class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        a = n % 2
        n = n // 2
        while n > 0:
            b = n % 2
            if (a == 1 and b == 0) or (a == 0 and b == 1):
                n = n // 2
                a = b
            else:
                return False
        return True
