# leetcode
# https://leetcode-cn.com/problems/find-and-replace-pattern/submissions/
# 转换成通用格式

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def fmt(word):
            count = 0
            m = {}
            s = ''
            for i in word:
                if i not in m:
                    m[i] = str(count)
                    count += 1
                s += m[i]
            return s

        ret = []
        m = fmt(pattern)
        for word in words:
            if fmt(word) == m:
                ret.append(word)
        return ret
