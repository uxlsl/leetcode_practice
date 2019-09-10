class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def f(board, visited, x, y):
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                if visited[x][y]:
                    return True
                if board[x][y] == "X":
                    return True
                visited[x][y] = True
                can = (
                    f(board, visited, x - 1, y)
                    and f(board, visited, x + 1, y)
                    and f(board, visited, x, y - 1)
                    and f(board, visited, x, y + 1)
                )
                if can:
                    board[x][y] = "X"
                return can
            else:
                return False

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    f(board, visited, x, y)
