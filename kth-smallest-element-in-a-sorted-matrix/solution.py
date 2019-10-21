class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lst = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lst.append(matrix[i][j])

        return sorted(lst)[k-1]
