# leetcode
# 左右更新结果

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ret = [float('inf')]*len(S)

        for index,c in enumerate(S):
            if c == C:
                i = index
                while i >= 0 and ret[i] != 0:
                    ret[i]=min(index-i,ret[i])
                    i -= 1

                i = index+1
                while i < len(S) and ret[i] != 0:
                    ret[i]=min(i-index,ret[i])
                    i += 1

        return ret
