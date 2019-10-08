class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def f(s):
            ret = [0] * 26
            for c in s:
                ret[index(c)] += 1
            return ret

        def index(c):
            return ord(c) - ord('a')

        if len(s1) > len(s2):
            return False
        s2 += 'a'
        x = f(s1)
        y = f(s2[:len(s1)])

        for i in range(1,len(s2)-len(s1)+1):
            if x == y:
                return True
            y[index(s2[i-1])] -= 1
            y[index(s2[i+len(s1)-1])] += 1

        return False
