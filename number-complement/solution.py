class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        i = 0
        while num > 0:
            if num & 1 == 0:
                ret |= 1<<i
            num = num >> 1
            i += 1
        return ret
