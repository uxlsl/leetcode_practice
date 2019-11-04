# leetcode
# https://leetcode-cn.com/problems/length-of-longest-fibonacci-subsequence/

# 暴力


class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        X = {}
        for i, v in enumerate(A):
            X[v] = i

        max_len = 0

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x, y = i, j
                cur = 2
                while True:
                    v = A[x] + A[y]
                    if v in X and X[v] > y:
                        x, y = y, X[v]
                        cur += 1
                    else:
                        break

                if cur > 2 and max_len < cur:
                    max_len = cur

        return max_len

    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 解法二
        # i-j-k
        from collections import defaultdict

        index = {v:i for i,v in enumerate(A)}
        X = defaultdict(lambda :2)
        ret = 2

        for k,v in enumerate(A):
            for j in range(k):
                i = index.get(v-A[j], None)
                if i is not None and i<j:
                    X[j,k] = X[i,j]+1
                    ret = max(X[j,k], ret)
        return ret if ret > 2 else 0
