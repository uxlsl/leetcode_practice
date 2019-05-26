from solution import Solution


def test_solution():
    s = Solution()
    assert s.maxProduct([-1, -2, -9, -6]) == 108
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
