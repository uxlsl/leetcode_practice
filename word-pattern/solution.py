class Solution(object):
    def wordPattern(self, pattern, str1):
        """
        :type pattern: str
        :type str: str
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

        if len(pattern) != len(str1.split()):
            return False

        for x,y in zip(change(pattern), change(str1.split())):
            if x != y:
                return False
        return True
