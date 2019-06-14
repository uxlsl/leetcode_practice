# leetcode 1041
# https://leetcode-cn.com/problems/robot-bounded-in-circle/



class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direct = 90
        x,y = 0,0

        while True:
            for i in instructions:
                if i == 'G':
                    if direct == 0:
                        x += 1
                    elif direct == 90:
                        y += 1
                    elif direct == 180:
                        x -= 1
                    else:# direct == 180:
                        y -= 1
                elif i == 'L':
                    direct += 90
                    direct %= 360
                elif i == 'R':
                    direct -= 90
                    direct %= 360
                else:
                    pass

            # 回到原状态就返回正确
            if x == 0 and y == 0:
                return True

            if direct == 90:
                return False
