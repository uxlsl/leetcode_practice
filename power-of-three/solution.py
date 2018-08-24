class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 3:
            if n % 3 == 0:
                return self.isPowerOfThree(n / 3)
            else:
                return False
        elif n == 1:
            return True
        else:
            return False
