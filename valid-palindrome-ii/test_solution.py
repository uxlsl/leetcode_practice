from solution import Solution


def test_solution():
    s = Solution()
    assert s.validPalindrome('aba') == True
    assert s.validPalindrome('abca') == True

