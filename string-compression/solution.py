# leetcode 443
# https://leetcode-cn.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)

        chars.append(-1) # 增加哨兵
        cur = chars[0]
        num = 1
        cur_p = 0  # 当前字符的位置
        i  = 1

        while i < len(chars):
            if cur == chars[i]:
                num += 1
            else:
                chars[cur_p] = cur
                cur_p += 1
                if num > 1:
                    for c in str(num):
                        chars[cur_p] = c
                        cur_p += 1
                cur = chars[i]
                num = 1
            i += 1

        # chars.pop() # 删除哨兵
        del chars[cur_p:]
        return cur_p
