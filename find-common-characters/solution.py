# 查找常用字符
# https://leetcode-cn.com/problems/find-common-characters/
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        def count(s):
            m = {}
            for c in s:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
            return m

        if len(A) == 1:
            return list(A[0])

        m = count(A[0])
        i = 1
        while i < len(A):
            x = {}
            y = count(A[i])
            for j in set(m.keys()) & set(y.keys()):
                x[j] = min(m[j], y[j])
            m = x

            i += 1

        result = []
        for k,v in m.items():
            result.extend([k]*v)

        return result
