from solution import Solution


def test_solution():
    s = Solution()
    assert s.missingNumber([]) == None
    assert s.missingNumber([0]) == 1
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([3,0,1]) == 2
    assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8

