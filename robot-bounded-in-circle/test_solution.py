from solution import Solution


def test_solution():
    s = Solution()
    assert s.isRobotBounded('GGLLGG') == True
    assert s.isRobotBounded('GG') == True
    assert s.isRobotBounded('GL') == True
