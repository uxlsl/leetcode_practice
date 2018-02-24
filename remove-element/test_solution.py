from solution import Solution


def test_solution():
    s = Solution()
    assert s.removeElement([], 3) == 0
    assert s.removeElement([2], 3) == 1
    assert s.removeElement([3,2,2,3], 3) == 2
