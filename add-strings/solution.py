# leetcode 字符串相加
# https://leetcode-cn.com/problems/add-strings/

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return int(num1) + int(num2)
        # 逆序处理进位
        num1 = num1[::-1]
        num2 = num2[::-1]
        x = 0  # 记录当前位的距离
        y = 0  # 记录从上一位进来的
        result = ''
        while x < max(len(num1), len(num2)):
            if x < len(num1):
                i = ord(num1[x]) - ord('0')
            else:
                i = 0

            if x < len(num2):
                j = ord(num2[x]) - ord('0')
            else:
                j = 0

            print("before>" + result)
            result = str((i + j + y) % 10) + result
            print("after>" + result)
            y = (i + j + y) // 10
            x += 1

        if y > 0:
            result = str(y) + result

        return result
