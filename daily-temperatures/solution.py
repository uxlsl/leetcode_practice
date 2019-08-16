class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        m = {}
        stack = []

        for index, num in enumerate(T):
            print(stack)
            if stack:
                a = stack[-1]
                if T[a] < num:
                    while stack:
                        x = stack.pop()
                        if T[x] < num:
                            m[x] = index - x
                        else:
                            stack.append(x)
                            break
                else:
                    stack.append(index)
            stack.append(index)

        print(m)
        return [m.get(i, 0) for i in range(len(T))]
