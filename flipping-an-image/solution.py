class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        return [[0 if j == 1 else 1 for j in reversed(i)] for i in A]
