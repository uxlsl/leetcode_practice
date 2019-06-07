from solution import Solution


def test_solution():
    s = Solution()
    assert s.isLongPressedName(name = "alex", typed = "aaleex") == True
    assert s.isLongPressedName(name = "saeed", typed = "ssaaedd") == False
    assert s.isLongPressedName(name = "leelee", typed = "lleeelee") == True
    assert s.isLongPressedName(name = "laiden", typed = "laiden") == True
