class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        def f(s):
            s = sorted(s)
            c = s[0]

            i = 1
            while i < len(s):
                if s[i] != c:
                    break
                i += 1

            return i

        ret = []
        words = [f(w) for w in words]
        for q in queries:
            count = 0
            i = f(q)
            for w in words:
                if i < w:
                    count += 1
            ret.append(count)

        return ret


