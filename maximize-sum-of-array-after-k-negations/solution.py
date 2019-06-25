import heapq

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 最少的反转,然后就K-1,以此
        def f(A, K):
            if K <= 0:
                return sum(A)
            else:
                x = heapq.heappop(A)
                heapq.heappush(A, -x)
                return f(A,K-1)

        heapq.heapify(A)
        return f(A, K)

