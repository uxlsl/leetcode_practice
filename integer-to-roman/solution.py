class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        record = [
                (1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')]
        i = 0
        s = ''
        while num > 0:
            if i == 0 and num >= record[i][0] or record[i-1][0] > num >= record[i][0]:
                s += record[i][1]
                num -= record[i][0]
            else:
                i += 1
        return s
