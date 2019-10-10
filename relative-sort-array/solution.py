class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        m = {}
        res = []
        arr2_s = set(arr2)
        for i in arr1:
            if i not in arr2_s:
                res.append(i)
            elif i in m:
                m[i] += 1
            else:
                m[i] = 1
        ret = []
        for i in arr2:
            for _ in range(m[i]):
                ret.append(i)

        ret.extend(sorted(res))
        return ret

