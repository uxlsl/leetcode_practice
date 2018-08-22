from solution import Solution


def test_solution():
    s = Solution()
    assert s.romanToInt('III') == 3
    assert s.romanToInt('IV') == 4
    assert s.romanToInt('IX') == 9
    assert s.romanToInt('LVIII') == 58
    assert s.romanToInt('MCMXCIV') == 1994
