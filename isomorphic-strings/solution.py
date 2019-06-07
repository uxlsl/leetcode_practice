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
                if c in m:
                    result += str(m[c])
                else:
                    m[c] = count
                    count += 1

            return result

        return change(s) == change(t)
