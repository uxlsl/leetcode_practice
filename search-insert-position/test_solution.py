from solution import Solution


def test_solution():
    s = Solution()
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) ==  1
    assert s.searchInsert([1,3,5,6], 7) ==  4
    assert s.searchInsert([1,3,5,6], 0) ==  0
