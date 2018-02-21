# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
answer = None


def setGuess(num):
    global answer
    answer = num


def guess(num):
    global answer
    if answer < num:
        return -1
    elif answer > num:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 0, n
        while l < h:
            m = (l + h + 1) //2
            x = guess(m)
            if x == -1:
                h = m
            elif x == 1:
                l = m
            else:
                return m
        return h
