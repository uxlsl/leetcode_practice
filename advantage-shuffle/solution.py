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

    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B = [(i,val) for i,val in enumerate(B)]
        B = sorted(B, key=lambda x:x[1])
        res = sorted(A)
        fail = []
        A = []
        for i,val in B:
            while res:
                j = res.pop(0)
                if j > val:
                    A.append(i)
                    break
                else:
                    fail.append(j)
            else:
                break
        return A


