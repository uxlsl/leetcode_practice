class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import itertools
        ret = 0
        for a,b,c in itertools.permutations(A, 3):
            if a < b + c and b < a + c and c < a + b:
                ret = max(ret, a+b+c)

        return ret

