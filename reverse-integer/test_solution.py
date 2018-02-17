from solution import Solution


def test_solution():
    s = Solution()
    assert s.reverse(1) == 1
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
