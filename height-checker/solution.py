# leetcode
# https://leetcode-cn.com/problems/height-checker/

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights_1 = sorted(heights)
        return len(heights) - lcs(heights, heights_1 , len(heights), len(heights_1))
