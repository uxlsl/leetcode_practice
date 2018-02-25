class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        is_delete = False

        while i <= j:
            # print(s[i], i, s[j], j)
            if s[i] != s[j]:
                if is_delete:
                    return False
                else:
                    is_delete = True
                    #  前查几个
                    if s[i+1] == s[j] and (i+2 > j -1 or s[i+2] == s[j-1]):
                        # print('delete {}'.format(s[i]))
                        i += 1
                    elif s[i] == s[j-1] and (i+1 > j -2 or s[i+1] == s[j-2]):
                        # print('delete {}'.format(s[j]))
                        j -= 1
                    else:
                        return False
            i += 1
            j -= 1

        return True
