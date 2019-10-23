# leetcode
# https://leetcode-cn.com/problems/string-to-integer-atoi/


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        num = 0
        flag = 1
        str = str.strip()
        if str == '':
            return 0
        if str[0] in ('-', '+'):
            flag = {'-':-1, '+':1}[str[0]]
            str = str[1:]

        for c in str:
            if not c.isdigit():
                break
            num = num * 10 + int(c)

        num = num*flag
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num


