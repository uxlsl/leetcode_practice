from solution import Solution


def test_solution():
    s = Solution()
    assert s.containsNearbyDuplicate([1,0,1], 2) == True
    assert s.containsNearbyDuplicate([1,2,3,4,1], 1) == False
    assert s.containsNearbyDuplicate([1], 1) == False
