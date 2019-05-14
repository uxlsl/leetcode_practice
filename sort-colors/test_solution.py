from solution import Solution


def test_solution():
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    assert nums == [0,0,1,1,2,2]
