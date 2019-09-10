class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def same(a,b):
            count = 0
            for x,y in zip(a,b):
                if x == y:
                    count += 1
            return count

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        record = set([beginWord])
        begin = set([beginWord])
        x = 1

        while begin:
            tmp = set()
            for word in begin:
                for to in wordList - record:
                    if same(word, to) == len(word) - 1:
                        if to == endWord:
                            return x+1
                        tmp.add(to)
                        record.add(to)
            x += 1
            begin = tmp
        return 0
