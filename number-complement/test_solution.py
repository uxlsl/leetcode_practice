from solution import Solution


def test_solution():
    s = Solution()
    assert s.findComplement(5) == 2
    assert s.findComplement(1) == 0
