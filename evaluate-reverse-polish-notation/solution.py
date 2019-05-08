import operator

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        val = 0
        for c in tokens:
            if c in ('+', '-', '*', '/'):
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    result = a + b
                elif c == '-':
                    result = b - a
                elif c == '*':
                    result = a * b
                else:
                    result = int(operator.truediv(b, a))
                stack.append(result)
            else:
                stack.append(int(c))
        return stack.pop()
