from solution import Solution


def test_solution():
    s = Solution()
    assert s.longestPalindrome('abccccdd') == 7
    assert s.longestPalindrome('abc') == 1
    assert s.longestPalindrome('cabc') == 3
