class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        from collections import Counter

        ret = ''
        c = Counter(s)
        for i,j in c.most_common():
            ret += i*j

        return ret
