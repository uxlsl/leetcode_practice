class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 初始一
        # 不断递增
        # 如果只有陆地，海洋，则返回-1

        land = False
        area = False
        X = []
        area0 = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    land = True
                    X.append((x, y))
                else:
                    area = True
                    area0.add((x, y))

        if land and area:
            count = 0
            arounds = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while X:
                Y = []
                for x, y in X:
                    for i, j in arounds:
                        x1, y1 = x + i, y + j
                        if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
                            if grid[x1][y1] == 0 and (x1, y1) in area0:
                                area0.remove((x1, y1))
                                Y.append((x1, y1))
                count += 1
                X = Y
                if len(area0) == 0:
                    return count
        else:
            return -1
