from solution import Solution


def test_solution():
    s = Solution()
    assert s.addDigits(38) == 2
    assert s.addDigits(386) == 8
