# leetcode 482
# https://leetcode-cn.com/problems/license-key-formatting/

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.upper().split('-'))
        x = len(S) % K
        lst = []
        if x > 0:
            lst.append(S[:x])
        for i in range(x,len(S), K):
            lst.append(S[i:i+K:])

        return '-'.join(lst)
