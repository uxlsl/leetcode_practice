class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        count = 0
        for i in S:
            if i in J:
                count += 1

        return count
