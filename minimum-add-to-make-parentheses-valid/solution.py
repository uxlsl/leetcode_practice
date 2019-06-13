class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        def f(stack):
            if len(stack) == 0:
                return 0
            c = stack.pop()
            if c == ')':
                count = 0
                while len(stack) > 0:
                    c = stack.pop()
                    if c == '(':
                        pass
                    count += f(stack)
            else:
                count = 1 + f(stack)
            return count
        stack = list(S)
        count = 0
        while stack:
            count += f(stack)
        return count
