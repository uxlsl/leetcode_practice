# leetcode 942
# https://leetcode-cn.com/problems/di-string-match/

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) < 1:
            return []

        result = [0]
        i = 0
        for c in S:
            if c == 'I':
                result.append(result[i]+1)
            elif c == 'D':
                result.append(result[i]-1)

        return result
