class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                peak = i-1
                break
            elif A[i-1] == A[i]:
                return 0

        for i in range(peak,len(A)-1):
            if A[i] <= A[i+1]:
                return 0
        return peak

