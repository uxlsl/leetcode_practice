# leetcode
# https://leetcode-cn.com/problems/longest-palindromic-subsequence
# 根据最长公共子序列所得

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        import functools

        @functools.lru_cache(None)
        def f(s):
            if len(s) <= 1:
                return len(s)
            if s[0] == s[-1]:
                return f(s[1:-1]) + 2
            else:
                return max(
                        f(s[1:]),
                        f(s[:-1]))

        return f(s)
