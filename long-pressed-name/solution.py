# leetcode 925
# https://leetcode-cn.com/problems/long-pressed-name/

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name) > len(typed):
            return False
        if name[0] == typed[0]:
            i,j = 1,1
            while i < len(name) and j < len(typed):
                # 相同进入下一个对比
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                else:
                    # 进行滑动
                    if typed[j-1] == typed[j]:
                        while j < len(typed) and typed[j-1] == typed[j]:
                            j += 1
                    else:
                        return False

            while j < len(typed) and typed[j-1] == typed[j]:
                j += 1
            if i == len(name) and j == len(typed):
                return True
            else:
                return False
        else:
            return False
