from solution import Solution


def test_solution():
    s = Solution()
    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1
    assert s.pivotIndex([-1,-1,-1,0,1,1]) == 0
