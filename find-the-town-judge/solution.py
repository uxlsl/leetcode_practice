class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        if N == 1:
            return 1
        x = defaultdict(set) # 信任
        y = defaultdict(set) # 被信任

        for i,j in trust:
            x[i].add(j)
            y[j].add(i)

        for k,v in y.items():
            if len(v) == N -1 and len(x[k]) == 0:
                return v

        return -1
