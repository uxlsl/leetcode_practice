# leetcode
# https://leetcode-cn.com/problems/heaters/


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        rad = 0
        while True:
            if houses[i] < heaters[j]:
                if heaters[j] - houses[i] > rad:
                    rad = heaters[j] - houses[i]
                i += 1
            elif houses[i] > heaters[j]:
                if heaters[i] - houses[j] > rad:
                    rad = heaters[i] - houses[j]

        return
