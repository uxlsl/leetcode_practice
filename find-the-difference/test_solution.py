from solution import Solution


def test_solution():
    s = Solution()
    assert s.findTheDifference('abcd', 'abcde') == 'e'
