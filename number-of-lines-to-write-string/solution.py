class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        total = sum(widths[ord(c) - ord('a')] for c in S)
        if total % 100 == 0:
            return [total // 100, 0]
        else:
            return [total // 100 + 1, total % 100]

