class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        val = 0
        for i in range(len(A)):
            for j in reversed(range(i+1+val, len(A))):
                if A[i] <= A[j]:
                    val = max(val, j-i)
                    break

        return val

