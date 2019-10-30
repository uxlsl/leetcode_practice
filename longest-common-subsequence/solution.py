class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        import functools

        @functools.lru_cache(None)
        def lcs(text1, text2):
            if text1 == '' or text2 == '':
                return 0
            else:
                if text1[-1] == text2[-1]:
                    return lcs(text1[:-1], text2[:-1]) + 1
                else:
                    return max(
                            lcs(text1[:-1], text2),
                            lcs(text1, text2[:-1]))

        return lcs(text1, text2)

