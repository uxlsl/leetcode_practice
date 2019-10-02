class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows,cols = set(),set()
        H,W = len(matrix), len(matrix[0])

        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(H):
            for j in range(W):
                if i in rows or j in cols:
                    matrix[i][j] = 0

