class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {')': '(',
             '}': '{',
             ']':'['}
        keep = []
        for c in s:
            if c in '({[':
                keep.append(c)
            elif c in ')}]':
                try:
                    x = keep.pop()
                    if m[c] != x:
                        return False
                except (KeyError, IndexError):
                    return False

        if keep:
            return False
        return True
