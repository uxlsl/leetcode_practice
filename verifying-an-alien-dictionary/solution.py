# https://leetcode-cn.com/problems/verifying-an-alien-dictionary/
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        def cmp(a,b,m):

            l = min(len(a), len(b))

            for i in range(l):
                if m[a[i]] < m[b[i]]:
                    return -1
                elif m[a[i]] > m[b[i]]:
                    return 1

            if len(a) < len(b):
                return -1
            elif len(a) > len(b):
                return 1
            else:
                return 0

        m = {}
        for i,v in enumerate(order):
            m[v] = i

        i = 0
        while i < len(words) - 1:
            if cmp(words[i], words[i+1],m) > 0:
                return False
            i += 1
        return True
