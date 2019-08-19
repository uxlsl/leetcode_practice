# leetcode
# https://leetcode-cn.com/problems/triangle/

# [
# [2],
# [3,4],
# [6,5,7],
# [4,1,8,3]
# ]


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        pre = []
        if len(triangle) == 1:
            return min(triangle[0])
        for i in range(len(triangle)):
            if i == 0:
                pre = list(triangle[i])
            else:
                cur = []
                row = triangle[i]
                for j in range(len(row)):
                    if j == 0:
                        cur.append(row[0] + pre[0])
                    else:
                        if j < len(row)-1:
                            cur.append(min(pre[j-1], pre[j])+row[j])
                        else:
                            cur.append(pre[j-1]+row[j])
                ret = min(cur)
                pre = cur
        return ret
