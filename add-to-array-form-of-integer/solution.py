ass Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if K ==0:
            return A
        total = 0
        for i in A:
            total = total * 10
            total += i
        total += K
        result = []
        while total > 0:
            result.append(total % 10)
            total = total // 10

        return list(reversed(result))
