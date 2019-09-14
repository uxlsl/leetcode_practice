import operator

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def get_waterflow(matrix, units, arounds, op):
            ret = set(units)
            X = units
            while X:
                Y = []
                for i, j in X:
                    for z, k in arounds:
                        x, y = i + z, j + k
                        if (x, y) in ret:
                            continue
                        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                            if op(matrix[i][j], matrix[x][y]):
                                Y.append((x, y))
                                ret.add((x, y))
                X = Y
            return ret

        if len(matrix) == 0:
            return []

        pac = set()
        for i in range(len(matrix[0])):
            pac.add((0, i))

        for i in range(len(matrix)):
            pac.add((i, 0))

        atl = set()
        for i in range(len(matrix[0])):
            atl.add((len(matrix) - 1,i))

        for i in range(len(matrix)):
            atl.add((i, len(matrix[0]) - 1))

        arounds = [(1,0),(-1,0),(0,1),(0,-1)]
        A = get_waterflow(matrix, pac, arounds, operator.le)
        B = get_waterflow(matrix, atl, arounds, operator.le)

        # for i in range(len(matrix)):
            # for j in range(len(matrix[0])):
                # if (i,j) in A:
                    # print(1,end='')
                # else:
                    # print(0,end='')
            # print()

        # for i in range(len(matrix)):
            # for j in range(len(matrix[0])):
                # if (i,j) in B:
                    # print(1,end='')
                # else:
                    # print(0,end='')
            # print()
        return list(A & B)
