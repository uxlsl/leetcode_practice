# leetcode
# 从最长的开始拼



class Solution(object):
    def minimumLengthEncoding1(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set()
        for i in words:
            for j in range(len(i)):
                s.add(i[j:])

        return s

    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=lambda x:len(x),reverse=True)
        S = ''
        mem = set()
        for i in words:
            if i not in mem:
                for j in range(len(i)):
                    mem.add(i[j:])
                S += '{}#'.format(i)
        return len(S)
