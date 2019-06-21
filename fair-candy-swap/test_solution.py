from solution import Solution


def test_solution():
    s = Solution()
    assert s.fairCandySwap(A = [1,1], B = [2,2]) == [1,2]
    assert s.fairCandySwap(A = [1,2], B = [2,3]) == [1,2]
    assert s.fairCandySwap(A = [2], B = [1,3]) == [2,3]
    assert s.fairCandySwap(A = [1,2,5], B = [2,4]) == [5,4]
