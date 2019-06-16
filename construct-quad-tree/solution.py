"""
# Definition for a QuadTree node.
"""
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def is_same(grid, x1,y1,x2,y2):
            if x1 == x2 and y1 == y2:
                return True
            val = grid[x1][y1]
            for x in range(x1, x2+1):
                for y in range(y1,y2+1):
                    if grid[x][y] != val:
                        return False

            return True
        def print_grid(grid, x1,y1,x2,y2):
            print('#'*10)
            print(x1,y1,x2,y2)
            for x in range(x1, x2+1):
                for y in range(y1,y2+1):
                    print(grid[x][y], end=' ')
                print()
            print('#'*10)

        def f(grid,x1,y1,x2,y2):
            if is_same(grid,x1,y1,x2,y2):
                return Node(grid[x1][y1] == 1,True,None,None,None,None)
            else:
                x_mid = (x1+x2)//2
                y_mid = (y1+y2)//2
                # 对边界有点不确定
                return Node(-1, False,
                        f(grid, x1,y1, x_mid,y_mid),
                        f(grid,x1,y_mid+1, x_mid, y2),
                        f(grid,x_mid+1,y1, x2, y_mid),
                        f(grid,x_mid+1,y_mid+1, x2, y2),
                )

        return f(grid, 0,0,len(grid)-1, len(grid[0])-1)
