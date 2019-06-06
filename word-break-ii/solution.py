class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        def f(path, res):
            word = ''
            i = 0
            while i < max_word and i < len(res):
                word += res[i]
                if word in wordDict:
                    path.append(word)
                    mem[''.join(path)].append(' '.join(path))
                    f(path, res[i+1:])
                    path.pop()
                i += 1
        if wordDict:
            max_word = max(len(i) for i in wordDict)
        else:
            max_word = len(s)
        word_set = set(wordDict)
        word = ''
        mem = defaultdict(list) # 字符串对应的可能列表
        path = []

        f(path, s)

        return mem[s]
