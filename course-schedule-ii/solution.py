# leetcode
# https://leetcode-cn.com/problems/course-schedule-ii/


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict

        out_count = defaultdict(int)
        in_nodes = defaultdict(list)

        for i,j in prerequisites:
            out_count[i] += 1
            in_nodes[j].append(i)

        S = list(set(range(numCourses)) - set(out_count.keys()))

        ret = []
        while S:
            i = S.pop()
            ret.append(i)
            for j in in_nodes[i]:
                out_count[j]-=1
                if out_count[j] == 0:
                    S.append(j)

        if len(ret) == numCourses:
            return ret
        else:
            return []
