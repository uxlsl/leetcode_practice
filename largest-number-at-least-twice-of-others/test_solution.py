from solution import Solution


def test_solution():
    s = Solution()
    assert s.dominantIndex([3,6,1,0]) == 1
    assert s.dominantIndex([1,2,3,4]) == -1
    assert s.dominantIndex([0,0,0,1]) == 3
