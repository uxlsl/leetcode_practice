from solution import Solution


def test_solution():
    s = Solution()
    assert s.increasingTriplet([1, 2, 3, 4, 5])
    assert s.increasingTriplet([5, 4, 3, 2, 1])
