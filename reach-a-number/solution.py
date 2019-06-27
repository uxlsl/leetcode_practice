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
        if target < 0:
            target = -target
        import math
        n = int(math.sqrt(2*target)) - 3
        return f(n*(n+1)/2,target, n+1)

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        point, step = 0, 0
        target = abs(target)
        while target > point or (point >= target and (point - target)%2 != 0):
            step += 1
            point += step
        return step
