# leetcode 942
# https://leetcode-cn.com/problems/di-string-match/
# 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

# 返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

# 如果 S[i] == "I"，那么 A[i] < A[i+1]
# 如果 S[i] == "D"，那么 A[i] > A[i+1]
# https://leetcode-cn.com/problems/di-string-match/solution/zeng-jian-zi-fu-chuan-pi-pei-by-leetcode/

class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]

