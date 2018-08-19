class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return [""]
        lst = []
        for c in S:
            if 48 <= ord(c) <= 57:
                if lst:
                    lst = [j + c for j in lst]
                else:
                    lst = [c]
            else:
                if lst:
                    lst = [i + j for i in lst for j in [c.lower(), c.upper()]]
                else:
                    lst = [c.lower(), c.upper()]

        return lst
