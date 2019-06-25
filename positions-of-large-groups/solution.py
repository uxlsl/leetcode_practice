class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        S += "0"
        c = S[0]
        begin = 0
        for i in range(1, len(S)):
            if S[i] != c:
                c = S[i]
                if i - begin >= 3:
                    ret.append([begin, i - 1])
                begin = i
        return ret
