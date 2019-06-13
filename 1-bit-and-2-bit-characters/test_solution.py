from solution import Solution


def test_solution():
    s = Solution()
    assert s.isOneBitCharacter([1, 0, 0]) == True
    assert s.isOneBitCharacter([1, 1, 1, 0]) == False
