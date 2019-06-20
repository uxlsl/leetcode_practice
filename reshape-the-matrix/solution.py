# leetcode
# https://leetcode-cn.com/problems/reshape-the-matrix/comments/
# 解法
# 重排

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        def foo(nums):
            h = len(nums)
            w = len(nums[0])
            for i in range(h):
                for j in range(w):
                    yield nums[i][j]

        h = len(nums)
        w = len(nums[0])
        if h*w != r*c:
            # 无法进行转化
            return nums

        n_num = foo(nums)
        result = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(next(n_num))

            result.append(row)

        return result
