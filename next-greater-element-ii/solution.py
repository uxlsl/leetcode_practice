# leetcode
# https://leetcode-cn.com/problems/next-greater-element-ii/


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        stack = []
        nums2 = nums + nums

        for index,num in enumerate(nums2):
            if stack:
                i = stack[-1]
                if nums2[i] < num:
                    while stack:
                        j = stack.pop()
                        if nums2[j] < num:
                            m[j] = index
                        else:
                            stack.append(j)
                            break
                else:
                    stack.append(index)
            stack.append(index)

        print(m)
        ret = []

        for i in range(len(nums)):
            if i in m:
                ret.append(nums[m[i]])
            else:
                ret.append(-1)

        return ret
