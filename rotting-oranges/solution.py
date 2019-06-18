import time
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 值 0 代表空单元格；
        # 值 1 代表新鲜橘子；
        # 值 2 代表腐烂的橘子。

        # 只有每一分钟有新鲜橘子都会腐烂就一直运行
        import copy

        w = len(grid)
        h = len(grid[0])

        count = 0


        while True:
            has_new = False
            new_to_bad = False
            grid_next = copy.deepcopy(grid)
            for x in range(w):
                for y in range(h):
                    if grid[x][y] == 0:
                        pass
                    elif grid[x][y] == 1:
                        has_new = True
                    else: # grid[x][y] == 2
                        has_bad = True
                        if x - 1 >= 0 and grid_next[x-1][y]==1:
                            new_to_bad = True
                            grid_next[x-1][y] = 2
                        if x + 1 < w and grid_next[x+1][y]==1:
                            new_to_bad = True
                            grid_next[x+1][y] = 2
                        if y -1 >= 0  and grid_next[x][y-1]==1:
                            new_to_bad = True
                            grid_next[x][y-1] = 2
                        if y + 1 < h and grid_next[x][y+1]==1:
                            new_to_bad = True
                            grid_next[x][y+1] = 2
            if not new_to_bad:
                if has_new:
                    return -1
                else:
                    return count
            count += 1
            grid = grid_next
