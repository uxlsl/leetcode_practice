class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        cache = {0:0}
        l = [0]
        while True:
            tmp = []
            nofound = True
            for i in l:
                for coin in coins:
                    if i + coin not in cache:
                        if i + coin <  amount:
                            nofound = False
                        if i + coin == amount:
                            return cache[i] + 1
                        cache[i+coin] = cache[i]+1
                        tmp.append(i+coin)
            if nofound:
                return -1
            l = tmp
