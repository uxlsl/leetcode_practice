from solution import Solution


def test_solution():
    s = Solution()
    assert s.findShortestSubArray([1, 2, 2, 3, 1]) == 2
    assert s.findShortestSubArray([1,2,2,3,1,4,2]) == 6
