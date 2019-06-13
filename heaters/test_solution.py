from solution import Solution


def test_solution():
    s = Solution()
    assert s.findRadius([1,2,3],[2]) == 1
    assert s.findRadius([1,2,3,4],[1,4]) == 1
