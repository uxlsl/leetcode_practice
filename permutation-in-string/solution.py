class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1 = ''.join(sorted(s1))

        for i in range(len(s2)-len(s1)+1):
            s = s2[i:i+len(s1)]
            if ''.join(sorted(s)) == s1:
                return True

        return False
