from solution import Solution


def test_solution():
    s = Solution()
    assert s.projectionArea([[2]]) == 5
    assert s.projectionArea([[1,2],[3,4]]) == 17
    assert s.projectionArea([[1,0],[0,2]]) == 8
    assert s.projectionArea([[1,1,1],[1,0,1],[1,1,1]]) == 14
    assert s.projectionArea([[2,2,2],[2,1,2],[2,2,2]]) == 21

