class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = set()
        t = list(t)
        for i1,v1 in enumerate(s):
            for i2,v2 in enumerate(t[i1:]):
                if v1 == v2:
                    pass
                else:
                    if i2 in record:
                        return False
                    else:
                        t[i2] = v1
                        record.add(i2)
        return s == ''.join(t)
