from solution import Solution


def test_solution():
    s = Solution()
    assert s.calculate('3+2*2') == 7
    assert s.calculate('3/2') == 1
    assert s.calculate('3+5/2') == 5
