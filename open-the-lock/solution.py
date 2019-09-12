class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def turn(s):
            for i in range(len(s)):
                c = int(s[i])
                yield s[:i] + str((c+1)%10) + s[i+1:]
                yield s[:i] + str((c-1)%10) + s[i+1:]

        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        queue = ['0000']
        mem = set(['0000'])
        count = 0

        while queue:
            count += 1
            queue_next = []
            for i in queue:
                for j in turn(i):
                    if j == target:
                        return count
                    if j in deadends:
                        continue
                    if j not in mem:
                        queue_next.append(j)
                    mem.add(j)
            queue = queue_next
        return -1
