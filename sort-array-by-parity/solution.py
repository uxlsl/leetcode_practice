# leetcode 905
# https://leetcode-cn.com/problems/sort-array-by-parity/
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        results = []

        for i in A:
            if i % 2 == 0:
                results.insert(0,i)
            else:
                results.append(i)
        return results
