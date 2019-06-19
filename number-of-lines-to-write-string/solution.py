class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        total = 0
        for c in S:
            total_n =  total + widths[ord(c) - ord('a')]
            if total_n % 100 != 0 and total//100 != total_n//100:
                total = total + 100 - total % 100 + widths[ord(c) - ord('a')]
            else:
                total = total_n
        return  [total // 100 + 1, total % 100]
