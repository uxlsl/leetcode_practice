# leetcode
# 310 -> 299
# 320 -> 299
# 330 -> 299
# 340 -> 339

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = list(str(N))
        nine = len(N)
        for i in range(len(N) - 1, 0, -1):
            if N[i - 1] > N[i]:
                N[i - 1] = str(int(N[i - 1]) - 1)
                nine = i

        N = ''.join(N)
        N = int(N[:nine] + '9' * (len(N) - nine))
        return N
