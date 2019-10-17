class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        m = {}

        for i in A:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for i in [B,C,D]:
            tmp = {}
            for j in i:
                for k,v in m.items():
                    if j + k not in tmp:
                        tmp[j+k] = v
                    else:
                        tmp[j+k] += v
            m = tmp
        return m.get(0, 0)