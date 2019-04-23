from solution import Solution


def test_solution():
    s = Solution()
    assert s.scoreOfParentheses('()') == 1
    assert s.scoreOfParentheses('(())') == 2
    assert s.scoreOfParentheses('()()') == 2
    assert s.scoreOfParentheses('(()(()))') == 6
