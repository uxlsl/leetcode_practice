# leetcode
# 能否分四分的问题


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def f(s, current, result):
            if len(current) ==4:
                if s == '':
                    result.append('.'.join(current))
                return
            num = ''
            for i in range(len(s)):
                num += s[i]
                if 0<=int(num)<256:
                    current.append(num)
                    f(s[i+1:],current,result)
                    current.pop()
                if num == '0':
                    break

        result = []
        f(s, [], result)
        return result
