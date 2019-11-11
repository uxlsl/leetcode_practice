class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # 先进后出
        # 01背包问题
        # 这个问题，以前没思考过
        # 递归能解决这个问题
        # 考虑pop出来的值

        def f(pushed, popped):
            if len(pushed) == 0:
                return True

            stack = []
            while pushed:
                v = pushed.pop(0)
                if v == popped[0]:
                    popped.pop(0)
                else:
                    stack.append(v)

                # 压进去，马上pop
                while stack and stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)

            stack = stack[::-1]
            if stack == popped:
                return True
            else:
                return False

        if len(pushed) != len(popped):
            return False

        return f(pushed, popped)
