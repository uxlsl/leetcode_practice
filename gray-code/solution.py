class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def f(n):
            if n == 0:
                return [0]
            if n == 1:
                return [0, 1]
            else:
                lst = f(n-1)
                ret = list(lst)
                for i in reversed(lst):
                    ret.append(i|(1<<(n-1)))
                return ret
        return f(n)
