from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        x = Counter(s1)

        for i in range(len(s2)-len(s1)+1):
            y = Counter(s2[i:i+len(s1)])
            if x == y:
                return True

        return False
