from solution import Solution


def test_solution():
    s = Solution()
    assert s.minAddToMakeValid('())') == 1
    assert s.minAddToMakeValid('(((') == 3
    assert s.minAddToMakeValid('()') == 0
    assert s.minAddToMakeValid('()))((') == 4
