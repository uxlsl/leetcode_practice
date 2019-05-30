from solution import Solution


def test_solution():
    s = Solution()
    assert s.findLengthOfLCIS([1,3,5,4,7]) == 3
    assert s.findLengthOfLCIS([2,2,2,2,2]) == 1
