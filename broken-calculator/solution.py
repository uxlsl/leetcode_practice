# leetcode
# https://leetcode-cn.com/problems/broken-calculator/


class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """

        def f(X, Y):
            if X == Y:
                return 0
            if X > Y:
                return X - Y

            # X < Y
            else:
                if X * 2 > Y:
                    # Y/2
                    ret = f(2 * X, Y)+1
                    if Y/2 <= X-1:
                        ret = min(ret, f(X - 1, Y) + 1)
                    return ret
                else:
                    # 优化这里
                    return 1 + f(2 * X, Y)

        return f(X, Y)
