class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        a = [nums[0]]
        x = nums[0]  # 保存当前最小值

        for i in range(1, len(nums)):
            if a[-1] < nums[i]:
                a.append(nums[i])
            elif len(a) == 2 and a[0] < nums[i] < a[1]:
                a[1] = nums[i]
            if len(a) >= 3:
                return True
            if x > nums[i]:
                x = nums[i]
            elif x < nums[i] and x < a[0]:
                a = [x, nums[i]]
        return False
