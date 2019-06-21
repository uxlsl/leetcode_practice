from solution import Solution


def test_solution():
    s = Solution()
    assert s.countBinarySubstrings("00110011") == 6
    assert s.countBinarySubstrings("10101") == 6
