class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2 = sorted([(i,v) for i,v in enumerate(nums2)],key=lambda x:x[1])
        m = {}

        for i in range(len(nums2)-1):
            m[nums2[i][1]] = nums2[i+1]

        ret = []
        for index,v in enumerate(nums1):
            if v in m:
                while v in m:
                    if m[v][0] > index:
                        ret.append(m[v][1])
                        break
                    v = m[v][1]
                else:
                    ret.append(-1)


            else:
                ret.append(-1)

        return ret
