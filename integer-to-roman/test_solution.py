from solution import Solution


def test_solution():
    s = Solution()
    assert s.intToRoman(3) == 'III'
    assert s.intToRoman(4) == 'IV'
    assert s.intToRoman(9) == 'IX'
    assert s.intToRoman(58) == 'LVIII'
    assert s.intToRoman(1994) == 'MCMXCIV'
