from solution import Solution


def test_solution():
    s = Solution()
    assert s.isPowerOfTwo(1) == True
    assert s.isPowerOfTwo(16) == True
    assert s.isPowerOfTwo(218) == False

