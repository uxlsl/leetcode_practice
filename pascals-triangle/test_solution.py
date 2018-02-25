from solution import Solution


def test_solution():
    s = Solution()
    x = [
            [1],
            [1,1],
            [1,2,1],
            [1,3,3,1],
            [1,4,6,4,1]
            ]
    assert s.generate(5) == x
