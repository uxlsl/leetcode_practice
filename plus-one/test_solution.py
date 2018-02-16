from solution import Solution


def test_solution():
    s = Solution()
    assert s.plusOne([1]) == [2]
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([1, 2, 9]) == [1, 3, 0]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
