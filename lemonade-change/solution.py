class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        moneys = {5:0, 10:0, 20:0}
        for i in bills:
            moneys[i] += 1
            if i > 5:
                last = i - 5
                if last > 10:
                    x = min(moneys[10],last // 10)
                    moneys[10] -= x
                    last -= x * 10
                if last > 0:
                    x = min(moneys[5], last // 5)
                    moneys[5] -= x
                    last -= x * 5
                if last > 0:
                    return False
        return True
