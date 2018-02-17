class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            flag = 1
        else:
            x = -x
            flag = -1
        lst = []
        while True:
            if x == 0:
                break
            lst.append(x % 10)
            x = x // 10
        ret = 0
        for index, v in enumerate(reversed(lst), 1):
            if v != 0:
                ret += v*10**(index-1)
        ret = flag * ret

        if -1(2**31 - 1) < ret < (2**31-1):
            return ret
        else:
            return 0
