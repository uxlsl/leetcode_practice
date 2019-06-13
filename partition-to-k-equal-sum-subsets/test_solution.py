from solution import Solution


def test_solution():
    s = Solution()
    assert s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) == True
