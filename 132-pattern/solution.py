# leetcode
# https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-2/


class Solution(object):
    def find132pattern1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if num[i] >= nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False

    def find132pattern2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 2):
            l = [nums[i]]
            for j in range(i + 1, len(nums)):
                if len(l) == 1:
                    if l[0] < nums[j]:
                        l.append(nums[j])
                else:
                    if l[1] < nums[j]:
                        l[1] = nums[j]
                    elif l[0] < nums[j] < l[1]:
                        return True

        return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        stack = []
        X = {}
        X[0] = nums[0]

        for i in range(1, len(nums)):
            X[i] = min(X[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > X[j]:
                while stack and stack[-1] <= X[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False
