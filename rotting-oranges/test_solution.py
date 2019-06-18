from solution import Solution


def test_solution():
    s = Solution()
    assert s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
