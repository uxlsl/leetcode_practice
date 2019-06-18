class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def is_str_factor(s1,s2):
            return s1 == (s2*(len(s1)//len(s2)))

        if len(str1) < len(str2):
            str1,str2 = str2,str1


        for i in range(len(str2), 1, -1):
            x = str2[:i]
            if len(str1) % i == 0 and len(str2) % i == 0 \
                    and is_str_factor(str1, x) and is_str_factor(str2, x):
                return x

        return ""
