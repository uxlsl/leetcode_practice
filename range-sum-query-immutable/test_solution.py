from solution import NumArray


def test_solution():
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    assert obj.sumRange(0, 2)  == 1
    assert obj.sumRange(0, 5)  == -3
    assert obj.sumRange(2, 5)  == -1

