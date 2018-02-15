from solution import Solution


def test_solution():
    s = Solution()
    assert s.titleToNumber('A') == 1
    assert s.titleToNumber('Z') == 26
    assert s.titleToNumber('AB') == 28
