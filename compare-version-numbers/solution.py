# leetcode
# 拼数子

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        a = version1.split('.')
        b = version2.split('.')

        i = 0

        while i < len(a) and i < len(b):
            if int(a[i]) > int(b[i]):
                return 1
            if int(a[i]) < int(b[i]):
                return -1
            i += 1

        if len(a) == len(b):
            return 0
        elif len(a) > len(b):
            for j in range(i,len(a)):
                if int(a[j]) != 0:
                    return 1
            else:
                return 0
        else:
            for j in range(i,len(b)):
                if int(b[j]) != 0:
                    return -1
            else:
                return 0
