from solution import Solution


def test_solution():
    s = Solution()
    assert s.peakIndexInMountainArray([0,1,0]) == 1
    assert s.peakIndexInMountainArray([0,2,1,0]) == 1
