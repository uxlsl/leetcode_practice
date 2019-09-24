class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)
        i = 0
        while k > 0 and i < len(num)-1:
            if int(num[i]) > int(num[i + 1]):
                del num[i]
                k -= 1
                if i > 0:
                    i -= 1
            else:
                i += 1

        for _ in range(k):
            if len(num) == 0:
                return "0"
            del num[-1]
        j = 0
        while j < len(num) and num[j] == "0":
            j += 1
        num = num[j:]
        if len(num) == 0:
            return "0"
        return "".join(num)
