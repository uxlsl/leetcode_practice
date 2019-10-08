class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import defaultdict
        m = defaultdict(int)

        for c in chars:
            m[c] += 1

        ret = 0
        for word in words:
            m1 = dict(m)
            for c in word:
                if c not in m1 or m1[c] - 1 < 0:
                    break
                m1[c] -= 1
            else:
                ret += len(word)
        return ret
