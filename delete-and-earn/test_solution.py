from solution import Solution


def test_solution():
    s = Solution()
    assert s.deleteAndEarn([3, 4, 2]) == 6
    assert s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
