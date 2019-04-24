from solution import Solution


def test_solution():
    s = Solution()
    assert s.canPartition([1, 5, 11, 5]) == True
    assert s.canPartition([1,2,3,5]) == False
