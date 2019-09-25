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
        n = str(N)
        num = []
        for i in n:
            num.append(i)

        nine = len(num)
        for i in range(len(num) - 1, 0, -1):
            if num[i - 1] > num[i]:
                num[i - 1] = str(int(num[i - 1]) - 1)
                nine = i

        num = ''.join(num)
        num = int(num[:nine] + '9' * (len(num) - nine))
        return num
