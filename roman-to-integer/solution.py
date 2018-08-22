class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
                'I'  : 1,
                'V'  : 5,
                'X'  : 10,
                'L'  : 50,
                'C'  : 100,
                'D'  : 500,
                'M'  : 1000,
                'IV' : 4,
                'IX' : 9,
                'XL' : 40,
                'XC' : 90,
                'CD' : 400,
                'CM' : 900,
            }
        num = 0
        while s != '':
            try:
                num += m[s[:2]]
                s = s[2:]
            except KeyError:
                num += m[s[0]]
                s = s[1:]
        return num

