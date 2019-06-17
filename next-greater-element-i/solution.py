class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2 = sorted(nums2)
        m = {}

        for i in range(len(nums2)-1):
            m[nums2[i]] = nums2[i+1]

        seen = set()
        ret = []

        for i,j in zip(nums1,nums2):
            seen.add(j)
            if i in m:
                while True:
                    if i in m:
                        if i not in seen:
                            ret.append(m[i])
                            break
                        i = m[i]
                    else:
                        ret.append(-1)
                        break

            else:
                ret.append(-1)

        return ret
