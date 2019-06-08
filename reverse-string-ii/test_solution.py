from solution import Solution


def test_solution():
    s = Solution()
    assert s.reverseStr("abcdefg", 2) == 'bacdfeg'
