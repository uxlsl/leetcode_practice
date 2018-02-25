from solution import Solution


def test_solution():
    s = Solution()
    a = [1,0]
    m = 1
    b = [2]
    n = 1
    s.merge(a, m, b, n)
    assert a == [1, 2]
    a = [1, 2, 3]
    b = [2.5]
    s.merge(a, 3, b, 1)
    assert a == [1, 2, 2.5, 3]
