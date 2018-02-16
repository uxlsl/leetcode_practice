from solution import Solution


def test_solution():
    s = Solution()
    assert s.firstUniqChar('leetcode') == 0
    assert s.firstUniqChar('loveleetcode') == 2
