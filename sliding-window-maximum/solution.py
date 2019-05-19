class Solution(object):
    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        stack = nums[:k]
        result = [max(stack)]
        for i in nums[k:]:
            stack.pop(0)
            stack.append(i)
            result.append(max(stack))
        return result

    def maxSlidingWindow(self, nums, k):
        if k == 0:
            return []
        result = []
        stack = []
        for index, value in enumerate(nums, 0):
            if stack:
                if stack[0][0] == index - k:
                    stack.pop(0)
                if stack and stack[-1][1] < value:
                    while stack and stack[-1][1] < value:
                        stack.pop()
            stack.append((index, value))
            if index - k + 1 >= 0:
                result.append(stack[0][1])
        return result
