class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = None
        nums.sort()
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                v = nums[i] + nums[j] + nums[k]
                if result == None:
                    result = v
                else:
                    if abs(v - target) < abs(result - target):
                        result = v
                diff = v - target
                if diff == 0:
                    return target
                elif diff > 0:
                    k -= 1
                else:  # v > 0
                    j += 1

            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return result
