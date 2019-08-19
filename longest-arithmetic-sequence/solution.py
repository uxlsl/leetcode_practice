class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        m = {}
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in m and m[diff][-1] == j:
                    m[diff].append(i)
                else:
                    m[diff] = [j, i]
                ret = max(len(m[diff]), ret)
        print(m)
        return ret
