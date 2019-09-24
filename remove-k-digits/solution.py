class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)

        for _ in range(k):
            if len(num) == 1:
                return '0'
            for i in range(len(num)-1):
                if int(num[i]) > int(num[i+1]):
                    del num[i]
                    break
            else:
                del num[-1]

        j = 0
        while j < len(num) and num[j] == '0':
            j += 1
        num = num[j:]
        if len(num) == 0:
            return '0'
        return ''.join(num)
