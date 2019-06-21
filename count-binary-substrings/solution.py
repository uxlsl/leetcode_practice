# leetcode
# https://leetcode-cn.com/problems/count-binary-substrings/
# 一些重复出现的子串要计算它们出现的次数

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # start + end ,start 等于1or0,end 等于1 or 0,比较数量
        count = 0
        i = 0
        while i < len(s):
            c = s[i]
            x = 1
            y = 0
            j = i + 1
            while j < len(s):
                if s[j] == c:
                    x += 1
                else:
                    y += 1
                    if x == y:
                        count += x
                        i += x
                        break
                j += 1
            else:
                i += 1
        return count
