from solution import Solution


def test_solution():
    s = Solution()
    assert s.isValid('{}') == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("([)]") == False
    assert s.isValid("){") == False
