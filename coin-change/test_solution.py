from solution import Solution


def test_solution():
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
