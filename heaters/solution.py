# leetcode
# https://leetcode-cn.com/problems/heaters/

# 很直观，就是编码
# 求半径最大值


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        x = 0
        y = 0
        rad = 0

        while x < len(houses):
            if houses[x] <= heaters[y]:
                rad = max(rad, heaters[y] - houses[x])
                x += 1
            else:
                if y < len(heaters) - 1:
                    if houses[x] <= heaters[y + 1]:
                        # 夹中间，看哪个最少
                        rad = max(
                            rad, min(houses[x] - heaters[y], heaters[y+1] - houses[x])
                        )
                        x += 1
                    else:
                        y += 1
                else:
                    # 已经到最后一个供暖器了
                    rad = max(rad, houses[-1] - heaters[y])
                    break
        return rad
