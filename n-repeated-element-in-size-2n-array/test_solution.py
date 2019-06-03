from solution import Solution


def test_solution():
    s = Solution()
    assert s.repeatedNTimes([1,2,3,3]) == 3
    assert s.repeatedNTimes([2,1,2,5,3,2]) == 2
    assert s.repeatedNTimes([5,1,5,2,5,3,5,4]) == 5
