class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 1
        x = A

        while len(x) <= 2*len(A)+len(B):
            if B in x:
                return i
            i += 1
            x += A

        return -1
