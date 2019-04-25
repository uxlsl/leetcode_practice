class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        cur = nums[0]
        count = 1
        length = 1

        for i in range(1,len(nums)):
            if cur == nums[i]:
                if count < 2:
                    nums[length] = cur
                    length += 1
                count += 1
            else:
                cur = nums[i]
                count = 1
                nums[length] = cur
                length += 1
        return length
