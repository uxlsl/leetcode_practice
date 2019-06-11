class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        z = int(c**0.5)
        for x in range(1,z):
            y = int((c - x*x)**0.5)
            if x*x + y * y == c:
                return True
        else:
            return False
