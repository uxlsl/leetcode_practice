class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def f(stack):
            if len(stack) == 0:
                return 1
            c = stack.pop()
            if c == ')':
                score = 0
                while stack:
                    c = stack.pop()
                    if c == '(':
                        if score == 0:
                            return 1
                        else:
                            return 2 * score
                    stack.append(c)
                    score += f(stack)
        stack = list(S)
        score = 0
        while stack:
            score += f(stack)
        return score
