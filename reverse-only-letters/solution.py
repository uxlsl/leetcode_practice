class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        R = [c for c in S if c.isalpha()]
        ret = ''
        for c in S:
            if c.isalpha():
                ret += R.pop()
            else:
                ret += c

        return ret
