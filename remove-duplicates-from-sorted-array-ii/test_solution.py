from solution import Solution


def test_solution():
    s = Solution()
    assert s.removeDuplicates([1,1,1,2,2,3]) == 5
    assert s.removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7
