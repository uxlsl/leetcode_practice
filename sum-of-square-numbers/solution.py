class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        # 使用math提高性能
        z = int(math.sqrt(c))
        for x in range(0,z+1):
            y = int(math.sqrt(c - x*x))
            if x*x + y * y == c:
                return True
        else:
            return False
