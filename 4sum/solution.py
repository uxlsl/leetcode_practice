class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                v = nums[i] + nums[j] + nums[k] - target
                if v == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    while j < len(nums) - 2 and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while k > 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                elif v > 0:
                    k -= 1
                else:  # v > 0
                    j += 1

            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return results

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        i = 0
        while i <= len(nums) - 4:
            three = self.threeSum(nums[i + 1:], target - nums[i])
            for l in three:
                results.append([nums[i]] + l)
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return results
