from solution import Solution


def test_solution():
    s = Solution()
    assert s.convertToTitle(1)  == 'A'
    assert s.convertToTitle(26)  == 'Z'
    assert s.convertToTitle(28)  == 'AB'
