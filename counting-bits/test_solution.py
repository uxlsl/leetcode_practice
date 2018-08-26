from solution import Solution


def test_solution():
    s = Solution()
    assert s.countBits(5) == [0,1,1,2,1,2]
