class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def getCoord(board, num):
            H = len(board)
            L = len(board[0])
            num = num -1
            i = H - num // L - 1
            if num // L % 2 != 0:
                j = L - num % L -1
            else:
                j = num % L
            return i,j

        H = len(board)
        L = len(board[0])
        #  (当前位置,使用蛇,使用梯)
        X = [(1, False,False)]
        visited = [False] * len(board)*len(board[0])
        count = 0

        while X:
            print(X, count)
            Y = []
            for item in X:
                x, y = getCoord(board, item[0])
                for i in range(1,7):
                    num = item[0] + i
                    if visited[num-1]:
                        continue
                    visited[num-1] = True
                    if num == H*L:
                        return count
                    pos = getCoord(board, num)
                    if board[pos[0]][pos[1]] >0:
                        #  蛇
                        if pos[0] == x and not item[1]:
                            Y.append((board[pos[0]][pos[1]], True, item[2]))
                        # 梯
                        elif not item[2]:
                            Y.append((board[pos[0]][pos[1]], item[1], True))
                    else:
                        Y.append((num, item[1], item[2]))
            X = Y
            count += 1

        return -1
