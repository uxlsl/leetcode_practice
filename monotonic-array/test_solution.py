from solution import Solution


def test_solution():
    s = Solution()
    assert s.isMonotonic([1,2,2,3]) == True
    assert s.isMonotonic([6,5,4,4]) == True
    assert s.isMonotonic([1,3,2]) == False
    assert s.isMonotonic([1,2,4,5]) == True
    assert s.isMonotonic([1,1,1]) == True

