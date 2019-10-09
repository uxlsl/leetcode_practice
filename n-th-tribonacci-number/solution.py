class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <=2:
            return 1
        T = [0] * (n + 1)
        T[0], T[1], T[2] = 0, 1, 1

        for i in range(3,n+1):
            T[i] = T[i-3]+T[i-2]+T[i-1]

        return T[-1]
