from solution import Solution


def test_solution():
    s = Solution()
    assert s.toHex(26) == '1a'
    assert s.toHex(-1) == 'ffffffff'
    assert s.toHex(0) == '0'
