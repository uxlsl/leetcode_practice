class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        k = k % len(nums)
        for _ in range(k):
            v = nums.pop()
            nums.insert(0, v)

