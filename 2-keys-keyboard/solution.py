import time
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(dp, step, num, clip):
            time.sleep(1)
            if num < len(dp):
                print(step, num, clip)
                if step < dp[num]:
                    dp[num] = step
                if clip > 0:
                    f(dp,step+1, num+clip, clip)
                f(dp,step+2, num, num)

        dp = [0] * (n+1)
        dp[1] = 1
        f(dp, 1,1,0)
        return dp[n]
