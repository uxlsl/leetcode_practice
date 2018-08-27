class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = {1: 1}
        for i in range(2, n + 1):
            record[i] = 1
            for j in range(1, (i + 1) // 2 + 1):
                record[i] = max(record[i], record[j] * record[i - j],
                                j * record[i - j], j * (i - j))
        return record[n]
