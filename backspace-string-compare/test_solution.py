from solution import Solution


def test_solution():
    s = Solution()
    assert s.backspaceCompare('ab#c', 'ad#c') == True
    assert s.backspaceCompare('ab##', 'c#d#') == True
    assert s.backspaceCompare('a##c', '#a#c') == True
    assert s.backspaceCompare('a#c', 'b') == False
