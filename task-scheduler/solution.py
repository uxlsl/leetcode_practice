class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        m = {}
        for i in tasks:
            if i not in m:
                m[i] = [0,0]
            m[i][1] += 1

        length = 0
        while m:
            for k,v in m.items():
                if length >= v[0]:
                    v[1] -= 1
                    length += 1
                    v[0] = length + n
                    if v[1] == 0:
                        del m[k]
                    break
            else:
                length += 1
        return length
