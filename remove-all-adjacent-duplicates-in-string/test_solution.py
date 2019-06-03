from solution import Solution


def test_solution():
    s = Solution()
    assert s.removeDuplicates('abbaca') == 'ca'
