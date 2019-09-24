class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {}

        for i,v in enumerate(S):
            last[v] = i

        last[' '] = -1

        ret = []
        start = 0
        end = last[S[0]]
        for i,v in enumerate(S[1:]+' ', 1):
            if i <= end:
                if last[v] > end:
                    end = last[v]
            else:
                ret.append(end - start+1)
                start = i
                end = last[v]

        return ret
