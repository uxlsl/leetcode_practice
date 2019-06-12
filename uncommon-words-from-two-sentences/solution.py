class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        def f(A,B):
            ret = []
            for i in set(A) - set(B):
                if A.count(i) == 1:
                    ret.append(i)

            return ret

        A = A.split()
        B = B.split()
        ret = f(A,B)
        ret += f(B,A)
        return ret

