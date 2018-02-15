from solution import Solution


def test_solution():
    s = Solution()
    assert s.removeDuplicates([]) == 0
    assert s.removeDuplicates([1]) == 1
    assert s.removeDuplicates([1,1,2]) == 2
    assert s.removeDuplicates([1,1,2,2]) == 2
    assert s.removeDuplicates([1,1,1,2]) == 2
    assert s.removeDuplicates([2, 3, 4]) == 3
