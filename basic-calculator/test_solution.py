from solution import Solution


def test_solution():
    s = Solution()
    assert s.calculate('1+1') == 2
    assert s.calculate('2-1+2') == 3
    assert s.calculate('(1+(4+5+2)-3)+(6+8)') == 23
