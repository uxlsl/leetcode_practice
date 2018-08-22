class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l = []
        r = []
        one_pos = None
        for i in range(len(seats)):
            if seats[i] == 1:
                one_pos = i
                l.append(0)
            else:
                if one_pos is not None:
                    l.append(i-one_pos)
                else:
                    l.append(None)

        one_pos = None
        for i in reversed(range(len(seats))):
            if seats[i] == 1:
                one_pos = i
                r.append(0)
            else:
                if one_pos is not None:
                    r.append(one_pos-i)
                else:
                    r.append(None)

        r = list(reversed(r))
        v = 0
        for i in range(len(seats)):
            if l[i] is None and r[i] is not None:
                x = r[i]
            elif l[i] is not None and r[i] is None:
                x = l[i]
            elif l[i] is None and r[i] is None:
                pass
            else:
                x = min(l[i], r[i])
            if v < x:
                v = x
        return v
