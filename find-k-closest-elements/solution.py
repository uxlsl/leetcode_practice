class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        return [
            arr[i]
            for i in sorted(
                sorted(list(range(len(arr))), key=lambda i: abs(arr[i] - x))[:k]
            )
        ]
