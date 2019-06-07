from solution import Solution


def test_solution():
    s = Solution()
    assert s.twoSum(numbers = [2, 7, 11, 15], target = 9) == [1,2]
