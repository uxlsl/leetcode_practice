class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n):
            if n == 1:
                return 0

            lst = []
            for i in range(2, n//2+1):
                if n % i == 0:
                    lst.append(f(n//i) + i + 1)
                    lst.append(f(i) + n//i)
            if lst:
                return min(lst)
            else:
                return n

        return f(n)
