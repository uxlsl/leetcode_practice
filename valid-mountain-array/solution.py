# leetcode 941
# https://leetcode-cn.com/problems/valid-mountain-array/
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        use = False
        direct = 1
        i = 0
        while i < len(A) - 1:
            if not (direct * A[i] < direct * A[i+1]):
                if use:
                    return False
                direct = -1
                use = True
                if i == 0:
                    return False
            else:
                i += 1
        return use

