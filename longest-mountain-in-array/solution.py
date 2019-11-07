class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_l = 0
        l = []
        flag = True  # True < False >
        A.append(float("inf"))
        for i in A:
            if l:
                if flag:
                    if l[-1] < i:
                        l.append(i)
                    elif l[-1] > i:
                        if len(l) >= 2:
                            flag = False
                            l.append(i)
                        else:
                            l = [i]
                    else:
                        l = [i]
                else:
                    if l[-1] > i:
                        l.append(i)
                    else:
                        max_l = max(max_l, len(l))
                        flag = True
                        if l[-1] < i:
                            l = [l[-1], i]
                        else:
                            l = [i]
            else:
                l.append(i)

        return max_l
