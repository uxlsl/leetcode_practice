class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        b = x ^ y
        while b > 0:
            b &=(b-1)
            count += 1
        return count

