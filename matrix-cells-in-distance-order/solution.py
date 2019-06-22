class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        m = [[i, j] for i in range(R) for j in range(C)]
        return sorted(m, key=lambda x: abs(r0 - x[0]) + abs(c0 - x[1]))
