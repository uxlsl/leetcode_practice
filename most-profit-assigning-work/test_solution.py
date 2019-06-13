from solution import Solution


def test_solution():
    s = Solution()
    assert s.leastInterval(["A","A","A","B","B","B"], 2)
