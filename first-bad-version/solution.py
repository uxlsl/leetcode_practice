# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):

    def setBadVersion_t(self, bad):
        self.bad = bad

    def isBadVersion_t(self, n):
        return self.bad <= n

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        x1 = 0
        x2 = n

        while True:
            m = (x1 + x2) // 2
            if self.isBadVersion(m):
                if x1 == m:
                    return x1
                x2 = m
            else:
                if x1 == m:
                    return x2
                x1 = m
