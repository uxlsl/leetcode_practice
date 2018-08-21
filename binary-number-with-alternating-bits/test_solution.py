from solution import Solution


def test_solution():
    s = Solution()
    assert s.hasAlternatingBits(5) == True
    assert s.hasAlternatingBits(7) == False
    assert s.hasAlternatingBits(11) == False
    assert s.hasAlternatingBits(10) == True
