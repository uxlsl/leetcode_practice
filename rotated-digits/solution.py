class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        m = {1:1, 0:0,2:5,5:2,6:9,8:8,9:6}
        ret = 0
        for n in range(1,N+1):
            y = ''
            for i in str(n):
                if int(i) in m:
                    y += str(m[int(i)])
                else:
                    break
            else:
                if y != str(n):
                    ret += 1
        return ret
