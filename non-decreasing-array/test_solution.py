from solution import Solution


def test_solution():
    s = Solution()
    assert s.checkPossibility([4,2,3]) == True
    assert s.checkPossibility([4,2,1]) == False
