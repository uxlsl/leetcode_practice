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
        for i in range(0, len(s)-1):
            c = s[i]
            x = 1
            y = 0
            i += 1
            while i < len(s):
                if s[i] == c:
                    x += 1
                else:
                    y += 1
                    if x == y:
                        count += 1
                        break
                i+=1
        return count
