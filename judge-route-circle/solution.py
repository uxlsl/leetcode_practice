class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        m = {}
        m['L'] = 1
        m['R'] = -1
        m['U'] = 1
        m['D'] = -1
        for i in moves:
            if i in 'LR':
                x += m[i]
            elif i in 'UD':
                y += m[i]
        if x == 0 and y == 0:
            return True
        else:
            return False

