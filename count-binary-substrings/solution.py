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
        m = {"0": "1", "1": "0"}
        count = 0
        i = 0
        while i < len(s):
            c = s[i]
            x = 0
            y = 0
            j = i
            while j < len(s) and s[j] == c:
                x += 1
                j += 1
            while j < len(s) and s[j] == m[c]:
                y += 1
                j += 1

            if x <= y:
                count += x
            else:  #  x > y:
                count += y
            i += x

        return count
