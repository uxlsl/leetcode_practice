from solution import Solution


def test_solution():
    s = Solution()
    assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
