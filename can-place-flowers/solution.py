# leetcode 605
# https://leetcode-cn.com/problems/can-place-flowers/


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        p = None
        q = 0
        ret = 0

        while q < len(flowerbed):
            if flowerbed[q] == 1:
                if p is not None: # 在10...01
                    x = q - p - 1
                    ret += (x - 1) // 2
                else:
                    # 0...1
                    ret += q // 2
                p = q
                print(ret)
                if ret >= n:
                    return True
            q += 1

        if p is not None:
            # 10.....
            if p < q:
                ret += (q - p - 1) // 2
        else:
            # 0....0
            if q % 2 == 0:
                ret = q // 2
            else:
                ret = q //2 + 1
        print(ret)
        return ret >= n
