# leetcode 896
# https://leetcode-cn.com/problems/monotonic-array
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 1:
            return True
        direct = 0
        i = A[0]
        for j in A[1:]:
            if i < j:
                if direct == 0:
                    direct = 1
                elif direct < 0:
                    return False
                else:
                    pass
            elif i > j:
                if direct == 0:
                    direct = -1
                elif direct > 0:
                    return False
                else:
                    pass
            pass
            i = j
        return True
