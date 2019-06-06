class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def f(s, path, word_set, results):
            if s == '':
                results.append(list(path))
                return
            word = ''
            i = 0
            while i < len(s):
                word +=s[i]
                if word in word_set:
                    path.append(word)
                    f(s[i+1:])
                    path.pop()
                i += 1

        results = []
        word_set = set(wordDict)
        path = []
        f(s,path, word_set, results)
        return [' '.join(i) for i in results]
