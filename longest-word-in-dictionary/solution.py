# leetcode
# https://leetcode-cn.com/problems/longest-word-in-dictionary/comments/
# 解法:
# 排序然后用set记录

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        mem = set()
        words = sorted(words)
        last = ''

        for word in words:
            if word[:-1] in mem or len(word) == 1:
                mem.add(word)
                if len(last) <len(word):
                    last = word
        return last
