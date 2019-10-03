class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        obstacles = set([tuple(i) for i in obstacles])
        cur = [0,0]
        while True:
            for cmd in command:
                if cmd == 'U':
                    cur[1] += 1
                elif cmd == 'R':
                    cur[0] += 1
                if tuple(cur) in obstacles:
                    return False
                if cur[0] == x and cur[1] == y:
                    return True
                if cur[0] > x and cur[1] > y:
                    return False

