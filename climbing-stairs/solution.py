class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
       """
        record = {
               0:1,
               1:1,
               }
        for i in range(2, n+1):
           record[i] = record[i-1] + record[i-2]
        return record[n]

