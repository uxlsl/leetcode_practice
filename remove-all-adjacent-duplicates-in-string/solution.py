# 1047. 删除字符串中的所有相邻重复项
# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []

        for c in S:
            if stack:
                x = stack.pop()
                if x != c:
                    stack.append(x)
                    stack.append(c)
            else:
                stack.append(c)

        return ''.join(stack)
