from solution import Solution


def test_solution():
    s = Solution()
    assert s.addBinary('11', '1') == '100'
