class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        if nums[0] > nums[1]:
            A = [0, 1]
        else:
            A = [1, 0]

        for i,v in enumerate(nums[2:], 2):
            if nums[A[1]] < v < nums[A[0]]:
                A[1] = i
            elif nums[A[0]] < v:
                j = A[0]
                A[0] = i
                A[1] = j
            else:
                pass
        if nums[A[0]] // 2 >= nums[A[1]]:
            return  A[0]
        else:
            return -1
