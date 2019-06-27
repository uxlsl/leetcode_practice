from solution import Solution


def test_solution():
    s = Solution()
    assert s.surfaceArea([[2]]) == 10
    assert s.surfaceArea([[1,2],[3,4]]) == 34
    assert s.surfaceArea([[1,0],[0,2]]) == 16
    assert s.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]) == 32
    assert s.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]) == 46


