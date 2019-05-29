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
        keys = [i[0] for i in
                sorted(m.items(), key=lambda x:x[1][1], reverse=True)]
        results = []
        while keys:
            for k in list(keys):
                if m[k][1] > 0 and length >= m[k][0]:
                    m[k][1] -= 1
                    if m[k][1] == 0:
                        keys.remove(k)
                    length += 1
                    m[k][0] = length + n
                    results.append(k)
                    break
            else:
                results.append('-')
                length += 1
        return results
