class Solution:
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == '':
            return True
        for word in wordDict:
            if s.startswith(word) and self.wordBreak(s[len(word):], wordDict):
                return True
        return False

    def wordBreak(self, s, wordDict):
        if wordDict:
            max_len = max(len(word) for word in wordDict)
        else:
            return False
        n = len(s)
        can_break = [False] * len(n+1)
        can_break[0] = True

        for i in range(1, len(s)+1):
            for l in xrange(1, min(i, max_len) + 1):
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break

        return can_break[-1]
