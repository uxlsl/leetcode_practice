class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
        x = min(A)
        y = max(A)

        if x + K > y - K:
            return 0
        else:
            return y-x-2*K
