class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 穷尽法,超时
        import functools

        @functools.lru_cache(None)
        def isPal(s):
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPal(s[i : j + 1]):
                    count += 1
        return count
