class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = set([
                'a','e', 'i','o','u',
                'A','E', 'I','O','U',
                ])
        vowels = [c for c in s if c in x]
        ret = ''

        for c in s:
            if c in x:
                ret += vowels.pop()
            else:
                ret += c

        return ret
