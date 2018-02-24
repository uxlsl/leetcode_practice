from solution import Solution


def test_solution():
    s = Solution()
    assert s.countAndSay(1) == '1'
    assert s.countAndSay(4) == '1211'

