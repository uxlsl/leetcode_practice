from solution import Solution


def test_solution():
    s = Solution()
    assert s.checkRecord('PPALLP') == True
    assert s.checkRecord('PPALLL') == False
