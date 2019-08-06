import copy


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def check_live(board, i, j):
            count = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    if (
                        0 <= i + x < len(board)
                        and 0 <= j + y < len(board[0])
                        and board[i + x][j + y] == 1
                    ):
                        count += 1
            return count

        backup = copy.deepcopy(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = check_live(backup, i, j)
                if backup[i][j] == 1:
                    if not 2 <= count <= 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1

