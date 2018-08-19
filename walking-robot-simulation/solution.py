class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        pos = [0,0]
        d = 90

        for i in commands:
            if i < 0:
                if i == -1:
                    d -= 90
                elif i == -2:
                    d += 90
            else:
                if d % 360 == 0:
                    pos[0] += i
                elif d %360 ==  90:
                    pos[1] += i
                elif d % 360 == 180:
                    pos[0] -= i
                elif d % 360 == 270:
                    pos[1] -= i

        return pos[0]*pos[0] + pos[1]*pos[1]
