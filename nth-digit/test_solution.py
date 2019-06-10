from solution import Solution


def test_solution():
    s = Solution()
    assert s.findNthDigit(3) == 3
    assert s.findNthDigit(11) == 0
