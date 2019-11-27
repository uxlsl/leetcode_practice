# leetcode
# https://leetcode-cn.com/problems/generate-parentheses/
# 我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，


class Solution(object):
    def generateParenthesis(self, N):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(S="", left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S + "(", left + 1, right)
            if right < left:
                backtrack(S + ")", left, right+1)

        backtrack()
        return ans
