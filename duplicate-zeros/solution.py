class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for i in arr:
            if i == 0:
                arr2.append(0)
            arr2.append(i)

        arr[:] = arr2[:len(arr)]
