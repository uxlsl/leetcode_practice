from solution import Solution


def test_solution():
    s = Solution()
    assert s.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1) == 11
