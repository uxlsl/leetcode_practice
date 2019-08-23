class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(side, start, visited):
            if start in visited:
                return False
            if start not in side:
                return True
            visited.add(start)
            for i in side[start]:
                if not dfs(side, i, visited):
                    return False
            visited.remove(start)
            return True

        side = {}
        for i,j in prerequisites:
            if i not in side:
                side[i] = []
            side[i].append(j)

        for i in range(numCourses):
            if i in side:
                if not dfs(side, i,set()):
                    return False
        return True
