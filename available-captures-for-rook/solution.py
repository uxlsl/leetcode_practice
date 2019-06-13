class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        H = len(board)
        W = len(board[0])

        for i in range(H):
            for j in range(W):
                if board[i][j] == 'R':
                    # 上下移动
                    # 上
                    count = 0
                    x,y = i-1, j

                    while x > 0:
                        if board[x][y] == '.':
                            x -=1
                        elif board[x][y] == 'B':
                            break
                        elif board[x][y] == 'p':
                            count += 1
                            break
                    # 下
                    x,y = i+1, j
                    while x < H:
                        if board[x][y] == '.':
                            x +=1
                        elif board[x][y] == 'B':
                            break
                        elif board[x][y] == 'p':
                            count += 1
                            break

                    # 左
                    x,y = i, j-1
                    while y > 0:
                        if board[x][y] == '.':
                            y -=1
                        elif board[x][y] == 'B':
                            break
                        elif board[x][y] == 'p':
                            count += 1
                            break

                    # 右
                    x,y = i, j+1
                    while y < W:
                        if board[x][y] == '.':
                            y +=1
                        elif board[x][y] == 'B':
                            break
                        elif board[x][y] == 'p':
                            count += 1
                            break

                    return count
