from solution import Solution


def test_solution():
    s = Solution()
    assert s.findPairs([3, 1, 4, 1, 5], 2) == 2
    assert s.findPairs([1, 2, 3, 4, 5], 1) == 4
    assert s.findPairs([1, 3, 1, 5, 4], 0) == 1
