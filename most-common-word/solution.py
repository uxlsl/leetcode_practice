# leetcode 819
# https://leetcode-cn.com/problems/most-common-word/


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        counts = {}
        banned = set(banned)
        word = ''

        for c in paragraph.lower() + ' ': # 加一个哨兵

            if 'a'<= c <= 'z':
                word += c

            if c in (' ', ',') and word:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
                word = ''

        for k,_ in sorted(counts.items(), key=lambda x:x[1], reverse=True):
            if k not in banned:
                return k
