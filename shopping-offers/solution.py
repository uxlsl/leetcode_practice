# leetcode
# 最多6种物品， 100种大礼包。
# 每种物品，你最多只需要购买6个。
# 你不可以购买超出待购清单的物品，即使更便宜。


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        N = len(price)
        # 子问题|大礼包|直接购买
        def f(needs):
            if sum(needs) == 0:
                return 0
            val = float('inf')
            direct = True
            for spe in special:
                total = 0
                needs_1 = []
                can = True
                for i in range(N):
                    if spe[i] > needs[i]:
                        can = False
                        break
                    total += spe[i]*price[i]
                    needs_1.append(needs[i] - spe[i])
                    # else:
                        # total += needs[i]*price[i]
                        # needs_1.append(0)

                if can and total > spe[-1]:
                    # 买礼包
                    val = min(f(needs_1) + spe[-1],val)
                    direct = False

            if direct:
                # 直接购买
                return sum(price[i]*needs[i] for i in range(N))
            else:
                return val

        return f(needs)
