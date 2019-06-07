class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def square(guess):
            return guess * guess

        def goodenough(guess, x):
            if abs(square(guess) - x) < 0.1:
                return True
            else:
                return False

        def improve(guess, x):
            return (x/guess + guess) / 2

        def sqrtIter(guess, x):
            if goodenough(guess, x):
                return guess
            else:
                return sqrtIter(improve(guess, x), x)

        return (num - int(sqrtIter(1,num))**2) == 0
