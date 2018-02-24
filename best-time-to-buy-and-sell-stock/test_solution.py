from solution import Solution


def test_solution():
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
