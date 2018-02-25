from solution import Solution


def test_solution():
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    assert nums == [5,6,7,1,2,3,4]
