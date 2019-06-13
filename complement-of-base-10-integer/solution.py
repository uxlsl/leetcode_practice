class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        lst = []
        while N > 0:
            if N & 1:
                lst.append(0)
            else:
                lst.append(1)
            N = N >> 1
        return sum(j*2**i for i,j in enumerate(lst))


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = len(bin(N)) - 2
        return 2**x - N - 1
