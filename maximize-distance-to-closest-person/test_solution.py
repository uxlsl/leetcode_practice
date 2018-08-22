from solution import Solution


def test_solution():
    s = Solution()
    assert s.maxDistToClosest([1,0,0,0,1,0,1]) == 2
