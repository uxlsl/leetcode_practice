from solution import Solution


def test_solution():
    s = Solution()
    assert s.moveZeroes([0, 1, 0, 3, 12]) ==  [1, 3, 12, 0, 0]
