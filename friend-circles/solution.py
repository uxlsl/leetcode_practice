class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        cricle = {}
        N = len(M)

        for i in range(N):
            for j in range(N):
                if M[i][j] != 1:
                    continue
                if i in cricle:
                    if j in cricle:
                        for k in cricle[j]:
                            cricle[i].add(k)
                            cricle[k] = cricle[i]
                    else:
                        cricle[i].add(j)
                        cricle[j] = cricle[i]
                else:
                    if j in cricle:
                        cricle[j].add(i)
                        cricle[i] = cricle[j]
                    else:
                        cricle[i] = cricle[j] = {i,j}
        return len(set([id(i) for i in cricle.values()]))
