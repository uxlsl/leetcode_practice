from solution import Solution


def test_solution():
    s = Solution()
    assert s.twoSum([3,3], 6) == [0,1]
