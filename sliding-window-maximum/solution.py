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
        stack = [(0,nums[0])]
        for index,value in enumerate(nums[1:]):
            if stack[-1][1] < value:
                while stack:
                    if stack[-1][1] < value:
                        stack.pop()
                    else:
                        stack.append((index, value))
                        break
                if len(stack) == 0:
                    stack.append((index, value))
            print(stack)
            result.append(stack[0][1])
        return result
