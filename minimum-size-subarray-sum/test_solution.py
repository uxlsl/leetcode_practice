from solution import Solution


def test_solution():
    s = Solution()
    assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
