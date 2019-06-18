class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        stack = []

        for num in nums2:
            if stack:
                a = stack[-1]
                if a < num:
                    while stack:
                        a = stack.pop()
                        if a < num:
                            m[a] = num
                        else:
                            stack.append(a)
                            break
                else:
                    stack.append(num)
            stack.append(num)

        ret = []

        for num in nums1:
            if num in m:
                ret.append(m[num])
            else:
                ret.append(-1)

        return ret

