import time
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        def f(to, target, n):
            if to == target:
                return n - 1
            if to + n<= target:
                return f(to+n, target,n+1)
            else:
                return f(to-n, target, n+1)
        return f(0,target, 1)
