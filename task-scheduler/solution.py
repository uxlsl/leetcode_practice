class Solution(object):
    def leastInterval_wrong(self, tasks, n):
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

    def leastInterval_wrong2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        results = []

        for task in tasks:
            pre_task = None
            for i in range(len(results)):
                if results[i] == task:
                    pre_task = i
                else:
                    if results[i] is None and pre_task is None or pre_task and pre_task + n < i:
                        results[i] = task
                        break
                    if pre_task and pre_task + n < i:
                        results.insert(i,task)
                        break
            else:
                if pre_task is not None:
                    for _ in range((pre_task +n) - len(results) + 1):
                        results.append(None)
                results.append(task)
        return len(results)

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        tmax = max(cnt.values())
        slots = (tmax - 1) * n
        tsum = len(tasks)
        return tsum + max(0, slots + tmax - 1 - sum(n - (n == tmax) for n in cnt.values()))
