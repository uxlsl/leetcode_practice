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
            print(pushed, popped)
            if len(pushed) == 0:
                return True
            stack = []
            while pushed:
                v = pushed.pop(0)
                if v == popped[0]:
                    popped.pop(0)
                    if stack and stack[-1] == popped[0]:
                        while stack:
                            i = stack.pop()
                            j = popped.pop(0)
                            if i != j:
                                return False
                        else:
                            if f(pushed, popped):
                                return True
                            else:
                                return False
                    else:
                        if f(pushed, popped):
                            while stack:
                                i = stack.pop()
                                j = popped.pop(0)
                                if i != j:
                                    return False
                            else:
                                return True
                        else:
                            return False
                else:
                    stack.append(v)
            else:
                return False

        if len(pushed) != len(popped):
            return False
        return f(pushed, popped)
