class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """

        dic = {}
        for i in hand:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        ks = sorted(dic.keys())

        while dic:
            k= ks.pop(0)
            while k in dic:
                for i in range(W):
                    x = k+i
                    if x not in dic:
                        return False
                    dic[x] -= 1
                    if dic[x] == 0:
                        del dic[x]
        return True
