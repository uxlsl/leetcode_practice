class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        def check_mine(board, x, y):
            arounds = [
                (-1, -1),
                (-1, 0),
                (0, -1),
                (1, -1),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            ]
            count = 0
            for i, j in arounds:
                x1, y1 = x + i, y + j
                if 0 <= x1 < len(board) and 0 <= y1 < len(board[0]):
                    if board[x1][y1] == "M":
                        count += 1
            return count

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        if board[click[0]][click[1]] == "E":
            mem = set()
            queue = [click]
            while queue:
                x, y = queue.pop(0)
                num = check_mine(board, x, y)
                if num == 0:
                    board[x][y] = "B"
                    arounds = [
                        (-1, -1),
                        (-1, 0),
                        (0, -1),
                        (1, -1),
                        (1, 0),
                        (-1, 1),
                        (0, 1),
                        (1, 1),
                    ]

                    for i, j in arounds:
                        x1, y1 = x + i, y + j
                        if 0 <= x1 < len(board) and 0 <= y1 < len(board[0]):
                            if (x1, y1) not in mem:
                                queue.append((x1, y1))
                                mem.add((x1, y1))
                else:
                    board[x][y] = str(num)
        return board
