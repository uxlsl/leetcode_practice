class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for c in ops:
            if c.isdigit() or c[1:].isdigit():
                scores.append(int(c))
            elif c == '+':
                scores.append(sum(scores[-2:]))
            elif c == 'D':
                scores.append(scores[-1]*2)
            elif c == 'C':
                scores.pop()
            else:
                pass
        return sum(scores)
