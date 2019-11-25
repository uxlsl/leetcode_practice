# leetcode
# 一个简单的解决方案是遍历该 9 x 9 数独 三 次，以确保：

# 行中没有重复的数字。
# 列中没有重复的数字。
# 3 x 3 子数独内没有重复的数字。

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                box_index = (i // 3 ) * 3 + j // 3

                rows[i][num] = rows[i].get(num,0) + 1
                columns[j][num] = columns[j].get(num,0) + 1
                boxes[box_index][num] = boxes[box_index].get(num,0) + 1

                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False

        return True
