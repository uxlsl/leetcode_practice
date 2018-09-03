class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def f(s):
            if s in results:
                return results[s]
            if s == '':
                return 1
            else:
                count = 0
                if s[0] in m:
                    count += f(s[1:])
                if len(s) > 1 and s[:2] in m:
                    count += f(s[2:])
                results[s] = count
                return count
        m = {}
        results = {}
        for i in range(ord('A'), ord('Z')+1):
            m[str(i-ord('A')+1)] = chr(i)
        return f(s)
