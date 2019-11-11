# leetcode
# https://leetcode-cn.com/problems/longest-well-performing-interval/


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        far = 0
        cur = 0
        l = 0

        for h in hours:
            if h > 8:
                cur += 1
            else:
                cur -= 1
            if cur > 0:
                l += 1
            else:
                cur = 0
                l = 0
            far = max(far, l)

        return far

    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        # 超时算法

        totals = [0]

        for i in hours:
            if i > 8:
                a = 1
            else:
                a = -1
            totals.append(totals[-1] + a)

        l = 0
        for i in range(len(hours)):
            for j in range(0, i+1):
                if totals[i + 1] - totals[j] > 0:
                    l = max(l, i - j + 1)
                    break
        return l
