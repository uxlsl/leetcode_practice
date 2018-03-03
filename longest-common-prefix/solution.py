class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        s = ''
        for l in zip(*strs):
            for i in l[1:]:
                if l[0] != i:
                    return s
            s += l[0]
        return s
