class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        m = {}
        for i in deck:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        if len(m.keys()) < 2 and list(m.values())[0] < 2:
            return False

        lst = sorted(m.items(), key=lambda x:x[1])
        num = lst[0][1]

        for x in range(2, num+1):
            for i in lst:
                if i[1] % x != 0:
                    break
            else:
                return True
        return False
