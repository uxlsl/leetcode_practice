class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A_count = 0
        C_continuous = 0

        for c in s:
            if c == 'A':
                A_count += 1
                if A_count > 1:
                    return False
            if c == 'L':
                C_continuous += 1
                if C_continuous > 2:
                    return False
            else:
                C_continuous = 0

        return True
