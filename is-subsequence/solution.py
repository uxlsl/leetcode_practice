class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        if not s:
            return True
        for i in t:
            if s:
                if i == s[0]:
                    s.pop(0)
                    if not s:
                        return True
        return False
