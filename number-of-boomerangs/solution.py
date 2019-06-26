# leetcode
# https://leetcode-cn.com/problems/number-of-boomerangs/submissions/
# 解法:通过等价距离,然后再排列

class Solution:
    def distance(self, p1, p2):
        # 注意 a**2 + b**2 比 a*a + b*b 耗时！
        return (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        res = 0
        for point in points:
            dic = dict()
            for tmp in points:
                if point != tmp:
                    dist = self.distance(point, tmp)
                    if dist not in dic:
                        dic[dist] = 1
                    else:
                        dic[dist] += 1
