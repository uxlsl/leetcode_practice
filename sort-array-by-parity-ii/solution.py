# leetcode 922
# https://leetcode-cn.com/submissions/detail/19812328/

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in sorted(A):
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        result = []
        for i,j in zip(even,odd):
            result.append(i)
            result.append(j)

        return result
