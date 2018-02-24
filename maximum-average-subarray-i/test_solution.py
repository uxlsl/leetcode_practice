from solution import Solution


def test_solution():
    s = Solution()
    assert s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
