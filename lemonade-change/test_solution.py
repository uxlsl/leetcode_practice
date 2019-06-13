from solution import Solution


def test_solution():
    s = Solution()
    assert s.lemonadeChange([5,5,5,10,20]) == True
    assert s.lemonadeChange([5,5,10]) == True
    assert s.lemonadeChange([5,5,10,10,20]) == False
