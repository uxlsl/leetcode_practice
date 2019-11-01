class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter

        c = Counter(words)
        m = {}
        for i,v in c.items():
            if v not in m:
                m[v] = []
            m[v].append(i)

        ret = []
        for i,v in sorted(m.items(), key=lambda x:x[0], reverse=True):
            ret.extend(sorted(v))

        return ret[:k]
