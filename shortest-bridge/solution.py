# leetcode
# https://leetcode-cn.com/problems/shortest-bridge/
# BFS


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 开始1旁边0开始

        def f(A, area, i, j):
            if 0 <= i < len(A) and 0 <= j < len(A[0]):
                if A[i][j] == 1 and tuple([i,j]) not in area:
                    area.add(tuple([i,j]))
                    f(A,area, i+1,j)
                    f(A,area, i-1,j)
                    f(A,area, i,j-1)
                    f(A,area, i,j+1)

        area = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    f(A,area, i,j)
                    break
            if area:
                break


        action = [[-1,0], [1,0], [0, -1], [0, 1]]
        count = 0

        side = set(area)

        while True:
            tmp = set()
            for i,j in side:
                for x,y in action:
                    p1,p2 = i+x, j+y
                    if 0<=p1<len(A) and 0<=p2<len(A[0]):
                        if tuple([p1,p2]) not in area:
                            if A[p1][p2] == 1:
                                return count
                            else:
                                tmp.add(tuple([p1,p2]))
                                area.add(tuple([p1,p2]))
            count += 1
            side = tmp
