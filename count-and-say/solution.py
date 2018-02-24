import re

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            x = s[0]
            count = 1
            tmp = ''
            for i in s[1:]:
                if x != i and count > 0:
                    tmp +=str(count) + x
                    x = i
                    count = 1
                else:
                    count += 1
            else:
                if len(s) == 1 or x == i:
                    tmp += str(count) + x

            s = tmp
        return s

