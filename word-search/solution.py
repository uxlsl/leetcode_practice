# leetcode
# https://leetcode-cn.com/problems/word-search/


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(word, start, board, i, j, visited):
            """
            word:
            start 下一个匹配点
            (i,j) 下一个点
            """

            if start == len(word):
                return True

            if 0<=i<len(board) and 0<=j<len(board[0]) and word[start] == board[i][j]:
                if visited[i][j]:
                    return False
                start += 1
                visited[i][j] = True
                # 上
                if dfs(word, start, board, i - 1, j, visited):
                    return True
                # 下
                elif dfs(word, start, board, i + 1, j, visited):
                    return True

                # 左
                elif dfs(word, start, board, i, j - 1, visited):
                    return True
                # 右
                elif dfs(word, start, board, i, j + 1, visited):
                    return True

                visited[i][j] = False

            return False

        visited = [[False for _ in range(len(board[i]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if dfs(word, 0, board, i, j, visited):
                        return True
        return False
