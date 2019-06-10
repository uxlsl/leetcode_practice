class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        m = {}
        for c in magazine:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

        for c in ransomNote:
            if c in m:
                m[c] -= 1
                if m[c] < 0:
                    return False
            else:
                return False

        return True
