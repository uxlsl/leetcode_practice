# leetcode
# https://leetcode-cn.com/problems/number-of-boomerangs/submissions/
# 解法:通过等价距离,然后再排列


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        m = defaultdict(lambda :defaultdict(list))

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                m[dist][i].append(j)
                m[dist][j].append(i)
        ret = 0
        for v in m.values():
            for vv in v.values():
                if len(vv) > 1:
                    ret += len(vv)*(len(vv)-1)

        return ret
