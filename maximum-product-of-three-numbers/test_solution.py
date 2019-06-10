from solution import Solution


def test_solution():
    s = Solution()
    assert s.maximumProduct([1,2,3]) == 6
    assert s.maximumProduct([1,2,3,4]) == 24
    assert s.maximumProduct([-1,-2,1,2,3]) == 6
