class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        L = len(matrix[0])
        H = len(matrix)
        ret = []
        x,y = 0, 0
        d = 0  # 表示方向
        for _ in range(L):
            i,j = x, y
            lst = []
            while 0<=i<H and 0<=j<L:
                lst.append(matrix[i][j])
                i += 1
                j -= 1
            if d % 2 == 0:
                lst.reverse()
            ret.extend(lst)
            y += 1
            d += 1

        x, y = 1,L-1

        for _ in range(H):
            i,j = x, y
            lst = []
            while 0<=i<H and 0<=j<L:
                lst.append(matrix[i][j])
                i += 1
                j -= 1
            if d % 2 == 0:
                lst.reverse()
            ret.extend(lst)
            x += 1
            d += 1

        return ret
