from solution import Solution


def test_solution():
    s = Solution()
    s.setBadVersion(6)
    assert s.firstBadVersion(9) == 6
    s.setBadVersion(1)
    assert s.firstBadVersion(9) == 1
