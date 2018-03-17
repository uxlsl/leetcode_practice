from solution import Solution


def test_solution():
    s = Solution()
    arr = ["5","2","C","D","+"]
    assert s.calPoints(arr) == 30
    arr = ["5","-2","4","C","D","9","+","+"]
    assert s.calPoints(arr) == 27
