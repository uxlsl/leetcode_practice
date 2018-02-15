
from solution import Solution


def test_solution():
    s = Solution()
    assert s.singleNumber([1]) == 1
    assert s.singleNumber([1,2,2]) == 1
    assert s.singleNumber([1,2,2,3,3]) == 1
    assert s.singleNumber([2,2,3,3, 1]) == 1

