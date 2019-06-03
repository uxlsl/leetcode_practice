# leetcode 1021
# https://leetcode-cn.com/problems/remove-outermost-parentheses

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        stack = []
        result = ''
        x = ''
        for c in S:
            x += c
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
                if len(stack) == 0:
                    if len(x) > 2:
                        result += x[1:-1]
                    x = ''
        return result
