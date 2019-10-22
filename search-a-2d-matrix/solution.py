class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if i == len(matrix) - 1 or matrix[i][0] <= target <= matrix[i + 1][0]:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True

        return False
