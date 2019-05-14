class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        one = 0
        two = 0
        zero = 0

        for num in nums:
            if num == 1:
                one += 1
            elif num == 2:
                two += 1
            else:
                zero += 1
        nums[0:zero] = [0]*zero
        nums[zero:zero+one] = [1]*one
        nums[zero+one:] = [2]*two
