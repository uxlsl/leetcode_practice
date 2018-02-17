from solution import Solution


def test_solution():
    s = Solution()
    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert s.maxSubArray([1]) == 1
