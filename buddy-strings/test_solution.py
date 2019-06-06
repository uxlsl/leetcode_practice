from solution import Solution


def test_solution():
    s = Solution()
    assert s.buddyStrings('ab', 'ba') == True
    assert s.buddyStrings('ab', 'ab') == False
    assert s.buddyStrings('aa', 'aa') == True
