# leetcode
# 每次找最少的数大于B


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        N = -1
        A = sorted(A)
        ret = []
        for i in B:
            for j in range(len(A)):
                if A[j] > i:
                    ret.append(A[j])
                    del A[j]
                    break
            else:
                ret.append(N)
        return [i if i != N else A.pop() for i in ret]
