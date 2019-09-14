class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        X = [(0, 0)]
        visited = {(0, 0): 0}
        arounds = [(-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0), (-1, 1), (0, 1), (1, 1)]

        while X:
            Y = []
            for x in X:
                for y in arounds:
                    i, j = x[0] + y[0], x[1] + y[1]
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                        if (
                            (i, j) in visited
                            #and visited[(i, j)] < visited[x] + 1
                            or grid[i][j] == 1
                        ):
                            continue
                        visited[(i, j)] = visited[x] + 1
                        Y.append((i, j))
            X = Y

        x = len(grid) - 1
        y = len(grid[0]) - 1
        if (x, y) in visited:
            return visited[(x, y)]
        return -1
