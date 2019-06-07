class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def change(s):
            m = {}
            count = 0
            result = ''
            for c in s:
                if c not in m:
                    m[c] = count
                    count += 1
                yield str(m[c])

            return result

        for x,y in zip(change(s), change(t)):
            if x != y:
                return False
        return True
