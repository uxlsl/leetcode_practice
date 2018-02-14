from solution import Solution



def test_solution():
    s = Solution()
    assert s.rob([1]) == 1
    assert s.rob([1,2]) == 2
    assert s.rob([1,2,3]) == 4
    assert s.rob([1,2,3,4]) == 6
    assert s.rob([4,2,3,1]) == 7
    assert s.rob([1,2,3,1,1]) == 5
