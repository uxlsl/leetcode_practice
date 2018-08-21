from solution import Solution


def test_solution():
    s = Solution()
    assert s.convertToBase7(100) == '202'
    assert s.convertToBase7(-7) == '-10'
