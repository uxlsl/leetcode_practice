from solution import Solution


def test_solution():
    s = Solution()
    assert s.findLHS([1,3,2,2,5,2,3,7]) == 5
    assert s.findLHS([1,2,3,4]) == 2
