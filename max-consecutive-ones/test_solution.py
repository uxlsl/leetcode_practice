from solution import Solution


def test_solution():
    s = Solution()
    assert s.findMaxConsecutiveOnes([1,1,0,1,1,1])  == 3
    assert s.findMaxConsecutiveOnes([1,1,1,1,1,0,1,1,1])  == 5
