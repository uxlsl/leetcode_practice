class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def avg_gray(M,i,j):
            total = 0
            num = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0 <= x < len(M) and 0 <= y < len(M[0]):
                        num += 1
                        total += M[x][y]
            return total // num

        result = []
        h = len(M)
        w = len(M[0])

        for i in range(h):
            row = []
            for j in range(w):
                row.append(avg_gray(M,i,j))

            result.append(row)

        return result
