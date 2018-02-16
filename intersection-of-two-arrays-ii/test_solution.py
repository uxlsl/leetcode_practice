from solution import Solution


def test_solution():
    s = Solution()
    assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
