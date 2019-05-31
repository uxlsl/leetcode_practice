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
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        length = len(A)

        if length < 3 or A[0] >= A[1]:
            return False

        index = 1
        while index < length - 1 and A[index - 1] < A[index]:
            index += 1
        while index < length and A[index - 1] > A[index]:
            index += 1
        return index == length
