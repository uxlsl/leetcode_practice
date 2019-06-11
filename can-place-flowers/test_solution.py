from solution import Solution


def test_solution():
    s = Solution()
    assert s.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert s.canPlaceFlowers([1,0,0,0,1], 2) == False
